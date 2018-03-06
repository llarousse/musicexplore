#!/usr/bin/env sh

export SCRAPY_SETTINGS_MODULE=scrapy_settings 
pwd
scrapy runspider allmusicspider.py
