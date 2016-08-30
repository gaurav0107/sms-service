"""
    Collection of helpful functions that can be used across the application.
"""
from flask import jsonify, g
import config
import time

# Checking if server is renning in the test environment
TEST_ENV = getattr(config, 'TEST_ENV', False)

def respond(response, http_status=200):
    """
        Utility function to respond to requests from the server.
        --
        Expects:
            -   response:                                       [MANDATORY]
                A 'dict' that contains your response. If this dict contains
                'http_status' as one of the indices, it is removed from the
                response object and placed in the HTTP header instead.
            -   http_status:                                    [OPTIONAL]
                An integer that signifies the HTTP response header. 200 by
                default, can be overridden by either supplying this second
                argument, or by supplying as 'http_status' index in response.
        --
        Returns:
            -   Your response from the server, minus the 'http_status' index,
                if present, which is returned in the HTTP header instead.

                Adds 'environment' = 'testing' to the response if running in
                testing environment.
    """
    response['response_timestamp'] = get_timestamp()
    if TEST_ENV:
        response['environment'] = 'testing'

    if 'http_status' in response:
        http_status = response['http_status']
        del response['http_status']

    g.request_end_time = get_timestamp()
    response['request_timestamp'] = g.request_start_time
    response['processing_time'] = g.processing_time()
    response['response_timestamp'] = g.request_end_time
    return jsonify(response), http_status

def decorate(response, request_timestamp):
    """
        Ideally, we would have a bunch of things that we always do to
        response objects here. I'm not sure about this function, might
        remove it later.
    """
    response['request_timestamp'] = request_timestamp
    return response

"""
    Tiny lambda give the current timestamp in milliseconds, needs no arguments.
"""
get_timestamp = lambda: int(time.time() * 1000)
