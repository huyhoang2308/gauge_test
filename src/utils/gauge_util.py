from getgauge.python import data_store

from src.utils import logger


class StoreDataUtil:

    @staticmethod
    def spec_store(keyword: str, data):
        logger.debug('specs storing %s \n %s' % (keyword, data))
        data_store.spec[keyword] = data

    @staticmethod
    def scenario_store(keyword: str, data):
        logger.debug('scenario storing %s \n %s' % (keyword, data))
        data_store.scenario[keyword] = data

    @staticmethod
    def suite_store(keyword: str, data):
        logger.debug('suite storing %s \n %s' % (keyword, data))
        data_store.suite[keyword] = data


class GetDataUtil:

    @staticmethod
    def spec_get(keyword: str):
        logger.debug('specs returns %s \n %s' % (keyword, data_store.spec.get(keyword)))
        return data_store.spec.get(keyword)

    @staticmethod
    def scenario_get(keyword: str):
        logger.debug('scenarios returns %s \n %s' % (keyword, data_store.scenario.get(keyword)))
        return data_store.scenario.get(keyword)

    @staticmethod
    def suite_get(keyword: str):
        logger.debug('suite returns %s \n %s' % (keyword, data_store.suite.get(keyword)))
        return data_store.suite.get(keyword)
