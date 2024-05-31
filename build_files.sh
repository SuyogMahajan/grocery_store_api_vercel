echo "Building Project"
python3 -m pip install -r requirements.txt

echo "Making Migration"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput 

echo "Collect Static"
python3 manage.py collectstatic --noinput --clear