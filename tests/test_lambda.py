from ..lambda_function import config_functions


def test_load_config():
    ORIGIN_GEODE_SOLUTIONS = 'https://geode-solutions.com'
    PATH_TOOLS_CREATE_BACKEND = '/tools/createbackend'
    config = config_functions.load_config(
        ORIGIN_GEODE_SOLUTIONS, PATH_TOOLS_CREATE_BACKEND)
    assert type(config) is dict
    assert type(config['SECURITY_GROUP']) is str
    assert type(config['SUBNET_ID']) is str
    assert type(config['VPC_ID']) is str
    assert type(config['SECONDS_BETWEEN_TRIES']) is float
    assert type(config['HEALTHCHECK_PORT']) is int
    assert type(config['LISTENER_ARN']) is str
    assert type(config['CLUSTER_NAME']) is str
    assert type(config['TASK_DEF_NAME']) is str
    assert type(config['ORIGINS']) is str

    # ORIGIN_GEODE_SOLUTIONS = 'https://geode-solutions.com'
    # PATH_TOOLS_CREATE_BACKEND = '/sharetwin/createbackend'
    # config = config_functions.load_config(
    #     ORIGIN_GEODE_SOLUTIONS, PATH_TOOLS_CREATE_BACKEND)
    # assert (config) == {
    #     'statusCode': 403,
    #     'statusDescription': '403 Forbidden',
    #     'isBase64Encoded': False,
    #     'headers': {
    #         'Access-Control-Allow-Headers': 'Content-Type',
    #         'Access-Control-Allow-Origin': '',
    #         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    #     }
    # }


def test_make_lambda_return():

    STATUS_CODE_200 = 200
    STATUS_DESCRIPTION_200 = '200 OK'
    ORIGIN_GEODE_SOLUTIONS = 'https://geode-solutions.com'

    lambda_return = config_functions.make_lambda_return(
        STATUS_CODE_200, STATUS_DESCRIPTION_200, ORIGIN_GEODE_SOLUTIONS)
    assert type(lambda_return) is dict
    assert lambda_return == {
        'statusCode': STATUS_CODE_200,
        'statusDescription': STATUS_DESCRIPTION_200,
        'isBase64Encoded': False,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': ORIGIN_GEODE_SOLUTIONS,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    BODY = dict({'ID': 123456})
    lambda_return = config_functions.make_lambda_return(
        STATUS_CODE_200, STATUS_DESCRIPTION_200, ORIGIN_GEODE_SOLUTIONS, BODY)
    assert type(lambda_return) is dict
    assert lambda_return == lambda_return == {
        'statusCode': STATUS_CODE_200,
        'statusDescription': STATUS_DESCRIPTION_200,
        'isBase64Encoded': False,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': ORIGIN_GEODE_SOLUTIONS,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': {
            'ID': 123456
        }
    }

    STATUS_CODE_403 = 403
    STATUS_DESCRIPTION_403 = '403 Forbidden'
    ORIGIN_EMPTY = ''
    BODY = {'error_message': 'Domain not allowed!'}
    lambda_return = config_functions.make_lambda_return(
        STATUS_CODE_403, STATUS_DESCRIPTION_403, ORIGIN_EMPTY, BODY)
    assert type(lambda_return) is dict
    assert lambda_return == lambda_return == {
        'statusCode': STATUS_CODE_403,
        'statusDescription': STATUS_DESCRIPTION_403,
        'isBase64Encoded': False,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': ORIGIN_EMPTY,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': BODY
    }
