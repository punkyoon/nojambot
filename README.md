# [DEPRECATED] nojambot

> 구글 어시스턴트에게 `헤이 구글, 재밌는 얘기 해줘` 혹은 `Hey Google, tell me a dad joke`를 말해보세요
> 
> 구글 때문에 더이상 이 프로젝트를 운영하지 않기로 결정했습니다 😢

## 소개

![nojambot_in_slack](https://user-images.githubusercontent.com/11442383/43994206-1e458d3a-9dd4-11e8-8a0b-b4bd12562539.png)

> 이제는 nojambot을 slack과 twitter에서 만나볼 수 있습니다!

twitter의 [@nojamrobot](https://twitter.com/nojamrobot)이 사용하는 봇의 코드입니다. 지금은 **overflow-club**에서 slack bot으로도 활동하고 있습니다.

@nojamrobot은 매 1시간 간격으로 랜덤한 노잼 개그를 트위터에 포스팅하고 있었습니다. ~그리고 정말 노잼이였는지, 망했습니다..~

지금은 **overflow-club**에서 slack bot으로 활동하고 있습니다. ~~얘도 망하려나 ㅠ~~

새로운 개그를 위해서는 여러분들의 도움이 절실합니다.

새로운 노잼 개그를 알고 계신 분은, [여기](https://github.com/punkyoon/nojambot/issues/1)에 제보해주세요!

## 사용방법

1. `conf.py`에 Consumer, Access token등의 값을 입력해줍니다.

> Twitter와 Slack에서 사용하는 값들이 다르니 유의해주세요.

2. `conf.py`의 `MINUTES`변수는 Twitter에서 동작하는 봇이 몇 분 간격으로 작동할 것인지 정해주는 항목입니다. 15분 간격으로 봇을 실행하고 싶으시다면, 다음과 같이 설정해주세요.

```python
...
MINUTES = 15
```

3. 봇을 실행하는 방법은 다음과 같습니다.

#### Twitter bot

```bash
python heart_of_bot.py twitter
```

#### Slack bot

```bash
python heart_of_bot.py slack
```

## License

[MIT license](https://github.com/punkyoon/nojambot/blob/master/LICENSE)

Copyright (c) 2021 punkyoon(Jiyoon Ha)
