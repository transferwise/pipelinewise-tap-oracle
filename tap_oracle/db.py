import singer
import cx_Oracle

LOGGER = singer.get_logger()

def fully_qualified_column_name(schema, table, column):
    return '"{}"."{}"."{}"'.format(schema, table, column)

def make_dsn(config):
    if config.get("service_name"):
        return cx_Oracle.makedsn(config["host"], config["port"], service_name=config.get("service_name"))
    else:
        return cx_Oracle.makedsn(config["host"], config["port"], sid=config.get("sid"))

def open_connection(config):
    LOGGER.info("dsn: %s", make_dsn(config))
    conn = cx_Oracle.connect(config["user"], config["password"], make_dsn(config))
    return conn
