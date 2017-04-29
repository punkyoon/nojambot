# nojambot

## twitter [@nojambot](https://twitter.com/nojamrobot)

twitter의 @nojambot이 사용하는 봇입니다.

## 사용방법

1. `conf.py`에 Consumer, Access token등의 값을 입력해줍니다.

2. `conf.py`의 `MINUTES`변수는 봇이 몇 분 간격으로 작동할 것인지 정해주는 항목입니다. 15분 간격으로 봇을 실행하고 싶으시다면, 다음과 같이 설정해주세요.

```python
...
MINUTES = 15
```

3. 다음 명령을 실행하면 봇이 작동합니다.
```bash
python bot.py
```

## License

[MIT license](https://github.com/punkyoon/nojambot/blob/master/LICENSE)

Copyright (c) 2017 punkyoon(Jiyoon Ha)
