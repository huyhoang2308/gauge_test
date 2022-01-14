import requests

from src.utils import logger


class RequestUtil:

    @staticmethod
    def post(url: str, headers: str, data):
        try:
            logger.debug('/POST url: %s \n header: %s \n data: %s' % (url, headers, data))
            r = requests.post(url, headers=headers, data=data)
            logger.debug(r.json())
            return r.json()
        except requests.exceptions.Timeout as timeoutErr:
            raise timeoutErr
        except Exception as e:
            raise e

    @staticmethod
    def get(url: str, headers: str, data=None):
        try:
            logger.debug('/GET url: %s \n header: %s \n data: %s' % (url, headers, data))
            r = requests.get(url, headers=headers, data=data)
            logger.debug(r.json())
            return r.json()
        except requests.exceptions.Timeout as timeoutErr:
            raise timeoutErr
        except Exception as e:
            raise e

    @staticmethod
    def put(url: str, headers: str, data):
        try:
            logger.debug('/PUT url: %s \n header: %s \n data: %s' % (url, headers, data))
            r = requests.put(url, headers=headers, data=data)
            logger.debug(r.json())
            return r.json()
        except requests.exceptions.Timeout as timeoutErr:
            raise timeoutErr
        except Exception as e:
            raise e

    @staticmethod
    def patch(url: str, headers: str, data):
        try:
            logger.debug('/PATCH url: %s \n header: %s \n data: %s' % (url, headers, data))
            r = requests.patch(url=url, headers=headers, data=data)
            logger.debug(r.json())
            return r.json()
        except requests.exceptions.Timeout as timeoutErr:
            raise timeoutErr
        except Exception as e:
            raise e

    @staticmethod
    def delete(url: str, headers: str, data):
        try:
            logger.debug('/DELETE url: %s \n header: %s \n data: %s' % (url, headers, data))
            r = requests.delete(url, headers=headers)
            logger.debug(r.json())
            return r.json()
        except requests.exceptions.Timeout as timeoutErr:
            raise timeoutErr
        except Exception as e:
            raise e
