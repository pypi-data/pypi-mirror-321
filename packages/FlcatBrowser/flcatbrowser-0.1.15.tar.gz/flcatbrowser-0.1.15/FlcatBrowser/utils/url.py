from urllib.parse import urlparse

def extract_domain(url):
    """
    从URL中提取域名部分。

    参数:
    url (str): 需要提取的URL。

    返回:
    str: 提取的域名。
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain