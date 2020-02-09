#!/usr/bin/env bash

frontend_target='build_dev'
backend_target='-d'

if [[ $1 = '-p' ]] || [[ $1 = '--production' ]]; then
  frontend_target='build_prod'
  backend_target='-p'
fi

cd `dirname $0`/..
npm --prefix frontend/ run ${frontend_target}
python bootstrap.py ${backend_target}
