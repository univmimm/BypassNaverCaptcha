# BypassNaverCaptcha
네*버 자동입력방지문자 뚫기

## 프로젝트의 시작
김종민한테 웹크롤링을 배우기 시작한 박성민..

첫 시작으로 셀레니움으로 네이버 로그인을 하려 하지만 네*버 자동입력방지에 막히고 마는데...!!

그래서 네*버 자동방지문자를 뜷는 프로젝트를 시작하기로 했다.

## 개발일지
## 19.07.23

네*버 자동방지를 피하기 위한 개발자들의 여러 방법이 있지만

우리는 자동 입력방지 이미지를 문자로 바꾸면 어떨까 했다. 

그래서 머신러닝을 사용해서 캡챠(자동입력방지문자이미지(너무길다))를 학습시키고

학습시킨 프로그램으로 이미지를 넣으면 문자를 출력하게 하려 했다.

하지만 생각외로 네*버 캡챠 이미지는 너무 복잡해보였고

그래서 대신 쉬운 이미지로 학습시켜 테스트 해본 다음 네*버 캡챠 이미지를 학습시키기로 했다

쉬운 이미지는 캡챠 생성 오픈소스를 찾아 김종민이 만들기로 했다. 


### <한 일 요약>
- 프로젝트 주제 정하기

- 오픈 소스 사용해서 captcha 코드 돌림
### <할 일 요약>
김종민 : captcha 이미지와 정답을 크롤링하여 서버에 저장하기.

박성민 : 머신러닝으로 어떻게 학습시킬지 방법 검색

## 19.07.24

머신러닝을 어떻게 할지 알아보던 와중 Tesseract에 대해 알게 됐다.

Tesseract는 오픈소스이고(야호), 이미지를 텍스트로 변환해주는 엔진이다

이 엔진을 사용하면 캡챠 이미지를 문자로 변환시켜주지 않을까 싶어 Tesseract로 캡챠 이미지를 돌려보기로 했다.

### <한 일 요약>
박성민

- 테서렉트 설치

김종민

- captcha 이미지를 서버에 저장했다!

### <할 일 요약>
박성민

- 테서렉트 파이썬으로 돌려보기


김종민

- python으로 10만장의 captcha 이미지와 답을 크롤링하여 서버에 저장하기.
- 머신 러닝을 학습 시키기 위한 알파벳 소,대문자와 숫자 (필요하다면 특수문자까지) 각 문자의 이미지 데이터를 수집 및 저장하기.
## 19.07.25
