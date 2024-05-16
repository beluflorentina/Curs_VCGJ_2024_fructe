#!/bin/sh
echo "Activare venv:"
#source .venv/bin/activate
. .venv/bin/activate
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=443_fructe
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5000 --reload
