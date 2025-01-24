from typing import Optional, get_args, get_type_hints, TypeVar, Any, get_origin, Union, TextIO
from enum import Enum
from dataclasses import dataclass, is_dataclass
import json
import os
from pydantic import BaseModel

T = TypeVar('T', bound=Union[dataclass, BaseModel])

def jsdc_load(fp: Union[str, TextIO], data_class: T, encoding: str = 'utf-8', max_size: int = 10 * 1024 * 1024) -> T:
    """
    Deserialize a file-like object containing a JSON document to a Python dataclass object.

    :param fp: A .read()-supporting file-like object containing a JSON document
    :param data_class: The dataclass type to deserialize into
    :param encoding: The encoding to use when reading the file (if fp is a string)
    :param max_size: Maximum allowed file size in bytes (default 10MB)
    :return: An instance of the data_class
    :raises: ValueError if file is too large or path is invalid
    :raises: FileNotFoundError if file doesn't exist
    :raises: PermissionError if file can't be accessed
    :raises: JSONDecodeError if JSON is malformed
    """
    if isinstance(fp, str):
        if not fp or not isinstance(fp, str):
            raise ValueError("Invalid file path")
        
        try:
            file_size = os.path.getsize(fp)
            if file_size > max_size:
                raise ValueError(f"File size {file_size} bytes exceeds maximum allowed size of {max_size} bytes")
            
            with open(fp, 'r', encoding=encoding) as f:
                return jsdc_loads(f.read(), data_class)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {fp}")
        except PermissionError:
            raise PermissionError(f"Permission denied accessing file: {fp}")
        except UnicodeDecodeError:
            raise ValueError(f"File encoding error. Expected {encoding} encoding")
    else:
        try:
            content = fp.read()
            if len(content.encode('utf-8')) > max_size:
                raise ValueError(f"Content size exceeds maximum allowed size of {max_size} bytes")
            return jsdc_loads(content, data_class)
        except Exception as e:
            raise ValueError(f"Error reading from file-like object: {str(e)}")

def jsdc_loads(s: str, data_class: T) -> T:
    """
    Deserialize a string containing a JSON document to a Python dataclass object.

    :param s: A string containing a JSON document
    :param data_class: The dataclass type to deserialize into
    :return: An instance of the data_class
    :raises: ValueError if input is invalid or type mismatch occurs
    :raises: TypeError if data_class is not a valid dataclass or BaseModel
    :raises: JSONDecodeError if JSON is malformed
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    if not s.strip():
        raise ValueError("Input string is empty or contains only whitespace")

    def validate_dataclass(cls: Any) -> None:
        if not cls:
            raise TypeError("data_class cannot be None")
        if not (is_dataclass(cls) or issubclass(cls, BaseModel)):
            raise TypeError('data_class must be a dataclass or a Pydantic BaseModel')

    def convert_dict_to_dataclass(data: dict, cls: T) -> T:
        if issubclass(cls, BaseModel):
            return cls.parse_obj(data)
        else:
            root_obj: T = cls()
            __dict_to_dataclass(root_obj, data)
            return root_obj

    def __dict_to_dataclass(c_obj: Any, c_data: dict) -> None:
        t_hints: dict = get_type_hints(type(c_obj))
        for key, value in c_data.items():
            if hasattr(c_obj, key):
                e_type = t_hints.get(key)
                if e_type is not None:
                    setattr(c_obj, key, convert_value(key, value, e_type))
            else:
                raise ValueError(f'Unknown data key: {key}')

    def convert_value(key: str, value: Any, e_type: Any) -> Any:
        if isinstance(e_type, type) and issubclass(e_type, Enum):
            return convert_enum(key, value, e_type)
        elif is_dataclass(e_type):
            return convert_dict_to_dataclass(value, e_type)
        elif get_origin(e_type) is list and is_dataclass(get_args(e_type)[0]):
            return convert_list_of_dataclasses(value, get_args(e_type)[0])
        else:
            return convert_other_types(key, value, e_type)

    def convert_enum(key: str, value: Any, enum_type: Any) -> Any:
        try:
            return enum_type[value]
        except KeyError:
            raise ValueError(f'Invalid Enum value for key {key}: {value}')

    def convert_list_of_dataclasses(value: list, item_type: Any) -> list:
        return [item_type(**item) for item in value]

    def convert_other_types(key: str, value: Any, e_type: Any) -> Any:
        try:
            origin = get_origin(e_type)
            if origin is Union:
                return convert_union_type(key, value, e_type)
            else:
                return convert_simple_type(key, value, e_type)
        except (ValueError, KeyError) as ex:
            raise ValueError(f'Invalid type for key {key}, expected {e_type}, got {type(value).__name__}') from ex

    def convert_union_type(key: str, value: Any, union_type: Any) -> Any:
        args = get_args(union_type)
        non_none_args = [arg for arg in args if arg is not type(None)]
        if len(non_none_args) == 1:
            actual_type = non_none_args[0]
            if isinstance(actual_type, type) and issubclass(actual_type, Enum):
                return actual_type[value]
            else:
                return actual_type(value)
        else:
            raise TypeError(f'Unsupported Union type for key {key}: {union_type}')

    def convert_simple_type(_: str, value: Any, e_type: Any) -> Any:
        if isinstance(e_type, type) and issubclass(e_type, Enum):
            return e_type[value]
        else:
            return e_type(value)

    try:
        data = json.loads(s)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        
        validate_dataclass(data_class)
        return convert_dict_to_dataclass(data, data_class)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error during deserialization: {str(e)}")

def jsdc_dump(obj: T, output_path: str, encoding: str = 'utf-8', indent: int = 4) -> None:
    """Serialize a dataclass or Pydantic BaseModel instance to a JSON file.

    This function takes a dataclass instance and writes its serialized 
    representation to a specified file in JSON format. The output file 
    can be encoded in a specified character encoding, and the JSON 
    output can be formatted with a specified indentation level.

    Args:
        obj (T): The dataclass instance to serialize.
        output_path (str): The path to the output file where the JSON 
                           data will be saved.
        encoding (str, optional): The character encoding to use for the 
                                  output file. Defaults to 'utf-8'.
        indent (int, optional): The number of spaces to use for indentation 
                                in the JSON output. Defaults to 4.

    Raises:
        ValueError: If the provided object is not a dataclass or path is invalid
        TypeError: If obj is not a dataclass or BaseModel
        OSError: If there are file system related errors
        UnicodeEncodeError: If encoding fails
    """
    if not output_path or not isinstance(output_path, str):
        raise ValueError("Invalid output path")
    
    if indent < 0:
        raise ValueError("Indent must be non-negative")

    def save_json_file(file_path: str, data: dict, encoding: str, indent: int) -> None:
        try:
            with open(file_path, 'w', encoding=encoding) as f:
                json.dump(obj=data, fp=f, indent=indent)
        except OSError as e:
            raise OSError(f"Failed to write to file {file_path}: {str(e)}")
        except UnicodeEncodeError as e:
            raise UnicodeEncodeError(f"Failed to encode data with {encoding}: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error during JSON serialization: {str(e)}")

    def validate_dataclass(cls: Any) -> None:
        if not (is_dataclass(cls) or issubclass(type(cls), BaseModel)):
            raise ValueError('obj must be a dataclass or a Pydantic BaseModel')

    def convert_dataclass_to_dict(obj: Any) -> Any:
        if isinstance(obj, BaseModel):
            return obj.dict()
        elif isinstance(obj, Enum):
            return obj.name
        elif isinstance(obj, list):
            return [convert_dataclass_to_dict(item) for item in obj]
        elif is_dataclass(obj):
            result = {}
            t_hints = get_type_hints(type(obj))
            for key, value in vars(obj).items():
                e_type = t_hints.get(key)
                if e_type is not None:
                    validate_type(key, value, e_type)
                result[key] = convert_dataclass_to_dict(value)
            return result
        return obj

    def validate_type(key: str, value: Any, e_type: Any) -> None:
        o_type = get_origin(e_type)
        if o_type is Union:
            if not any(isinstance(value, t) for t in get_args(e_type)):
                raise TypeError(f'Invalid type for key {key}: expected {e_type}, got {type(value)}')
        elif o_type is not None:
            if not isinstance(value, o_type):
                raise TypeError(f'Invalid type for key {key}: expected {o_type}, got {type(value)}')
        else:
            if not isinstance(value, e_type):
                raise TypeError(f'Invalid type for key {key}: expected {e_type}, got {type(value)}')

    try:
        # Ensure directory exists and is writable
        directory = os.path.dirname(os.path.abspath(output_path))
        if directory:
            if os.path.exists(directory):
                if not os.access(directory, os.W_OK):
                    raise OSError(f"No write permission for directory: {directory}")
            else:
                try:
                    os.makedirs(directory)
                except OSError as e:
                    raise OSError(f"Failed to create directory {directory}: {str(e)}")

        validate_dataclass(obj)
        data_dict = convert_dataclass_to_dict(obj)
        save_json_file(output_path, data_dict, encoding, indent)
    except OSError as e:
        raise OSError(f"Failed to create directory or access file: {str(e)}")
    except TypeError as e:
        raise TypeError(f"Type validation failed: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error during serialization: {str(e)}")

if __name__ == '__main__':
    from dataclasses import field
    from enum import auto
    import tempfile
    import os
    from typing import Dict, List

    # Test basic dataclass serialization/deserialization
    @dataclass 
    class DatabaseConfig:
        host: str = 'localhost'
        port: int = 3306
        user: str = 'root'
        password: str = 'password'
        ips: list[str] = field(default_factory=lambda: ['127.0.0.1'])
        primary_user: Optional[str] = field(default_factory=lambda: None)

    # Test with temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        temp_path = tf.name
        
    db = DatabaseConfig()
    jsdc_dump(db, temp_path)
    loaded_db = jsdc_load(temp_path, DatabaseConfig)
    assert db.host == loaded_db.host
    assert db.port == loaded_db.port
    assert db.ips == loaded_db.ips
    
    # Test enums
    @dataclass
    class UserType(Enum):
        ADMIN = auto()
        USER = auto()
        GUEST = auto()

    @dataclass 
    class UserConfig:
        name: str = 'John Doe'
        age: int = 30
        married: bool = False
        user_type: UserType = field(default_factory=lambda: UserType.USER)
        roles: list[str] = field(default_factory=lambda: ['read'])

    # Test nested dataclasses
    @dataclass
    class AppConfig:
        user: UserConfig = field(default_factory=lambda: UserConfig())
        database: DatabaseConfig = field(default_factory=lambda: DatabaseConfig())
        version: str = '1.0.0'
        debug: bool = False
        settings: dict[str, str] = field(default_factory=lambda: {'theme': 'dark'})

    # Test complex nested structure
    app = AppConfig()
    app.user.roles.append('write')
    app.database.ips.extend(['192.168.1.1', '10.0.0.1'])
    app.settings['language'] = 'en'
    
    jsdc_dump(app, temp_path)
    loaded_app = jsdc_load(temp_path, AppConfig)
    
    assert loaded_app.user.roles == ['read', 'write']
    assert loaded_app.database.ips == ['127.0.0.1', '192.168.1.1', '10.0.0.1']
    assert loaded_app.settings == {'theme': 'dark', 'language': 'en'}

    # Test Pydantic models
    class ServerConfig(BaseModel):
        name: str = "main"
        port: int = 8080
        ssl: bool = True
        headers: dict[str, str] = {"Content-Type": "application/json"}

    class ApiConfig(BaseModel):
        servers: List[ServerConfig] = []
        timeout: int = 30
        retries: int = 3

    # Test Pydantic model serialization/deserialization
    api_config = ApiConfig()
    api_config.servers.append(ServerConfig(name="backup", port=8081))
    api_config.servers.append(ServerConfig(name="dev", port=8082, ssl=False))
    
    jsdc_dump(api_config, temp_path)
    loaded_api = jsdc_load(temp_path, ApiConfig)
    
    assert len(loaded_api.servers) == 2
    assert loaded_api.servers[0].name == "backup"
    assert loaded_api.servers[1].port == 8082
    assert not loaded_api.servers[1].ssl

    # Test error cases
    try:
        jsdc_load("nonexistent.json", DatabaseConfig)
        assert False, "Should raise FileNotFoundError"
    except FileNotFoundError:
        pass

    try:
        jsdc_dump(DatabaseConfig(), "\\\\?\\invalid:path\\config.json")
        assert False, "Should raise OSError"
    except OSError:
        pass

    # Clean up
    os.remove(temp_path)
    print("All tests passed successfully!")
