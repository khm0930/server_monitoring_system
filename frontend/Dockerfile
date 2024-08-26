# 공식 Node.js 런타임 이미지를 기반으로 사용
FROM node:14

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# package.json 및 package-lock.json 파일을 컨테이너로 복사
COPY package.json /app/
COPY package-lock.json /app/

# package.json에 명시된 의존성 설치
RUN npm install

# 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사
COPY . /app/

# React 개발 서버를 위한 포트 3000 열기
EXPOSE 3000

# React 개발 서버를 실행하는 명령어
CMD ["npm", "start"]
