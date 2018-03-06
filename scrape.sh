#!/usr/bin/env sh

export SCRAPY_SETTINGS_MODULE=scrapy_settings 
export PYTHONPATH=/var/www/basicproject/basicproject
scrapy runspider allmusicspider.py
