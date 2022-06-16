#!/bin/bash

mkdir tempdir

cp -f assessment_code.py tempdir/.
cp -f network_equipment.json tempdir/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY  assessment_code.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY  network_equipment.json /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python /home/myapp/assessment_code.py &" >> tempdir/Dockerfile

cd tempdir
docker build -t assessmentcodeimage .
docker run -p 5050:5050 --name assessment2container assessmentcodeimage &
