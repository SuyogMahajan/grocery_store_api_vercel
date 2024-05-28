echo "Building Project"
python3.10 -m pip install -r requirement.txt

echo "Making Migration"
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput 

echo "Collect Static"
python3.10 manage.py collectstatic --noinput --clear