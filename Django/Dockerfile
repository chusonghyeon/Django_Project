# 파이썬 버전
FROM python:3.9.0

RUN mkdir /root/.ssh/

# 호스트 경로 / 컨테이너 경로
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

# 권한 주기
RUN chmod 600 /roor/.ssh/id_rsa

# 파일 생성
RUN touch /root/.ssh/known_hosts

#  ssh키 옮기기
RUN ssh-keyscan github.comm >> /root/.ssh/known_hosts

# 시작 디렉토리
WORKDIR /home/

RUN echo "testing"

#GIT에서 가져오기
# RUN git clone https://github.com/chusonghyeon/DJango_Pragmatic_Project.git

# SSH으로 GIR가져오기
RUN git clone git@github.com:chusonghyeon/DJango_Pragmatic_Project.git

# 장고 들어있는 디렉토리 접근
WORKDIR /home/DJango_Pragmatic_Project/

# env파일 생성
# RUN echo "SECRET_KEY = django-insecure-#e-f2tt3z$=95x=#v^c(4*_kx(z9^*wkd*1h7h-%#%23wl+$yt" > .env

# install한 파일들 다운받기
RUN pip install -r requirements.txt

# gunicorn 설치
RUN pip install gunicorn

# 마리아 DB설치
RUN pip install mysqlclient

# DB리셋(파일형 DB사용하였기 때문에 가능한것이다) -> CMD쪽으로 이동된다.
# RUN python manage.py migrate

# nginx에 연결하는 정적인 파일 실행 -> CMD쪽으로 이동된다.(마지막에 사용하기 위해)
# RUN pyhton manage.py collectstatic

# 포트지정
EXPOSE 8000

# gunicorn으로 runserver실행
# CMD ["python", "mangae.py", "runserver.py","0.0.0.0:8000"]

CMD ["bash", "-c", "pyhton manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
