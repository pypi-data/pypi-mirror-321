from .log import LoggingTool
from fastapi import Request
class Decorator:
    def __init__(self, log_path,token_middleware):
        self.logger = LoggingTool(log_path).setup_logger()
        self.token_middleware = token_middleware
    def func_exception(self,func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"在函数 {func.__name__} 中捕获到异常: {e}")

        return wrapper


    def func_requests(self,func):
        def wrapper(
            request: Request,
            data: dict = None,
        ):
            try:
                if not data:
                    data = {}
                token = request.headers.get("Authorization")
                self.logger.info(request.headers)
                if token:
                    res = self.token_middleware.jwt.decode_token(token)
                    if not res:
                        return {"errorcode": "9999", "msg": "token无效"}
                    data.update({"payload": res})
                else:
                    return {"errorcode": "9999", "msg": "token无效"}
            except Exception as e:
                return {"errorcode": "9999", "msg": "token无效"}
            try:
                data.update(
                    {
                        "request": request,
                    }
                )
                self.logger.info(
                    f""" 收到请求: {request.base_url}{request.url.path[1:]} 
                            
    请求来源: {request.client.host}
    请求地址: {request.base_url}{request.url.path[1:]}                        
    请求参数: {data}

                """
                )
                return func(data)
            except Exception as e:
                print(f"在函数 {func.__name__} 中捕获到异常: {e}")
                return {"errorcode": "9999", "msg": "未知错误"}

        return wrapper
