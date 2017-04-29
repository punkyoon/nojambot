# nojambot

## Twitter [@nojambot](https://twitter.com/nojamrobot)

twitter의 @nojambot이 사용하는 봇의 코드입니다.

@nojambot은 매 1시간 간격으로 랜덤한 노잼 개그를 트위터에 포스팅하고 있습니다.

새로운 개그를 위해서는 여러분들의 도움이 절실합니다.

새로운 노잼 개그를 알고 계신 분은, [여기](https://github.com/punkyoon/nojambot/issues/1)에 제보해주세요!

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
