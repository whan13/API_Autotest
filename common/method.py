import requests

#封装二次请求方法

class MyRequests:
    def __init__(self,base_url=None):
    #初始化时可以传入基础路径，例如："http://api.github.com"    pass
        self.session = requests.Session()
        self.base_url = base_url

    def request(self,method,url,**kwargs):
        # 核心请求方法，负责拼接url、统一发送请求、捕获异常
        #1、智能拼接URl
        #如果传入的是完整地址（http开头），直接用；否则拼接 base_url
        full_url = url if url.startswith('http') else f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        try:
            #2、统一调用session.request(支持所有请求动词)
            #methods.upper() 确保'get'自动变为'GET'
            response = self.session.request(method.upper(),full_url,**kwargs)

            #3、状态检查：如果返回 4xx 或5xx错误，抛出异常进入except
            response.raise_for_status()

            return response

        except requests.exceptions.RequestException as e:
            # 4、捕获异常：网络超时、400、500 等都会在这里统一报错
            print(f"[请求异常] 路径: {full_url} | 错误信息: {e}")
            return None
        
    # --- 下面是快捷调用方法 ---
    def get(self,url,**kwargs):
        return self.request('GET',url,**kwargs)
    
    def post(self,url,**kwargs):
        return self.request('POST',url,**kwargs)
    
    def put(self,url,**kwargs):
        return self.request('PUT',url,**kwargs)
    
    def delete(self,url,**kwargs):
        return self.request('DELETE',url,**kwargs)
    


# import requests

# class Requests():
#     def __init__(self):
#         self.session=requests.Session()

#     def request(self,url,method,**kwargs):
#         if method=='get':
#             return self.session.request(url=url,method=method,**kwargs)
#         elif method=='post':
#             return self.session.request(url=url,method=method,**kwargs)

#     def get(self,url,**kwargs):
#         return self.request(url=url,method='get',**kwargs)

#     def post(self,url,**kwargs):
#         return self.request(url=url, method='post', **kwargs)

