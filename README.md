2D게임그래픽 텀프로젝트
========================

2d게임그래픽 텀프로젝트 기말프로젝트 준비 / 게임공학부 엔턴테인먼트컴퓨팅전공 2017184017 오선재
----------------------------------

### 게임의 소개
* 제목   
  * 내세의 경계(經界)     

* 목적   
  * 악령(몬스터)의 공격을 회피 또는 선제공격으로 처치함으로서 게임오버가 되지 않게 하며 필요한 아이템들을 모아 숲을 탈출(게임 클리어) 한다.   

* 간단한 스토리      
  * 악령(몬스터)들이 가득한 음기 짙은 숲에 떨어지게 된 무녀(플레이어)는 숲을 탈출하려고 합니다. 하지만 이렇게 많은 악령들을 그냥 둘 수는 없겠지요, 자신이 숲에서 탈출하는 순간 따라나올지도 모르고.... 때문에 오래전 숲 곳곳에 흩어진, 봉인에 필요한 도구들을 모아 숲에서 나가는 순간 숲 전체를 봉인하려고 합니다. 악령들에게 공격받아 위험해지기(게임오버) 이전에 필요한 도구들을 전부 모아 숲을 성공적으로 봉인하고 탈출할수 있을까요?    

* 게임방법   
  * 특정키를 입력하면 무녀(플레이어)는 악령(몬스터)들을 공격할 수 있는 형태의 오브젝트를 쏘아냅니다. (슈팅게임 형식) 숲속에서 움직이는 동안 (플레이하는 동안) 다가오는 악령들을 피하거나, 혹은 공격하여 처치함으로서 게임오버가 되는것을 막아내며 숲속(필드) 곳곳에 있는 봉인도구들(필요 아이템)을 모으세요. 필요한 봉인도구들을 전부 다 모았다면, 숲의 끝(스테이지의 끝)에서 봉인을 성공적으로 마치고 탈출할 수 있을것입니다.    

***


### GameState(Scene)의 수와 이름    
1. 로고     
2. 타이틀     
3. 튜토리얼(게임방법 등)      
4. 메인게임(Game Stage)     
5. GameClear      
6. GameOver      

***


### 각 GameState별 설명
* GameState_1: 로고
  * KPU로고 및 제작자명을 띄우는 화면입니다.
  * 객체목록: 로고 화면(KPU, 2D게임그래픽 텀프로젝트, 게임공학부 엔턴테인먼트컴퓨팅전공 2017184017 오선재)
  * 이벤트: 일정 시간이 지나면 자동으로 다음 State로 넘어가는 이벤트
  * 이동조건: 일정 시간이 지날시 두번째 장면인 타이틀화면으로 넘어갑니다.

* GameState_2: 타이틀
  * 게임의 타이틀을 띄우는 화면입니다.
  * 객체목록: 타이틀화면, 게임 START 또는 게임방법 안내
  * 이벤트: 특정키를 입력시 게임 시작 또는 게임 방법화면으로 안내, 혹은 마우스 입력으로.
  * 이동조건: 게임 시작을 선택시 게임 시작 화면으로, 게임 방법을 선택시 게임 방법(튜토리얼)화면으로 넘어가며, 게임 클리어 또는 게임오버 이후 해당 화면으로 다시 돌아옵니다.

* GameState_3: 튜토리얼(게임방법)
  * 게임의 방법, 그러니까 튜토리얼을 띄우는 화면입니다.
  * 객체목록: 튜토리얼 화면(이미지), 게임 시작 안내
  * 이벤트: 특정키를 입력 또는 마우스 입력(이 경우 게임 시작ui추가)시 메인 게임 화면으로 넘어갑니다.
  * 이동조건: 타이틀화면에서 게임 방법 화면으로 넘어가는 조건 만족시 (특정 키 입력 또는 마우스 입력) 해당 화면으로 넘어오며, 마찬가지로 '게임 시작'에 해당하는 입력시 메인 게임 화면으로 넘어갑니다.

* GameState_4: 메인 게임(Game Stage)
  * 메인 게임이 진행되는 화면입니다.
  * 객체목록: 플레이어(무녀), 몬스터(악령), 공격 오브젝트(부적), 필요 아이템(봉인도구), 게임 맵, 기타 필요한 ui(hp상태표시 등)
  * 이벤트: 플레이어는 키보드 입력으로 움직이며, 특정 키를 입력시 플레이어가 향하고 있는 방향으로 오브젝트를 쏘아내 몬스터를 공격할수 있습니다. (키보드 입력 이벤트) 그 외에는 아이템과의 충돌체크를 통해 아이템을 자동으로 획득할수 있게 하거나 혹은 특정키 입력시 아이템을 획득할수 있는 이벤트,스테이지 마지막에서 특정키 입력시 아이템 사용 가능 이벤트. 전반적으로 키입력 이벤트가 주로 쓰일듯 합니다.
  * 이동조건: 게임 시작 화면에서 게임 시작을 선택 혹은 게임 방법화면에서 게임 시작을 선택할시 타이틀화면에서 해당화면으로 넘어옵니다.

* GameState_5: GameClear
  * 게임 클리어 결과를 띄우는 화면입니다.
  * 객체목록: 게임 클리어 화면(이미지), 타이틀화면으로의 안내.
  * 이벤트: 특정키를 입력시 게임 타이틀화면으로 돌아갑니다.
  * 이동조건: 메인 게임에서 클리어 조건 충족시 해당 화면으로 자동으로 넘어오며, 이후 키 입력을 통해 게임 타이틀화면으로 돌아갑니다.

* GameState_6: GameOver
  * 게임 오버 결과를 띄우는 화면입니다.
  * 객체목록: 게임 오버 화면(이미지), 타이틀화면으로의 안내.
  * 이벤트: 특정키를 입력시 게임 타이틀화면으로 돌아갑니다.
  * 이동조건: 메인 게임에서 게임오버 조건 충족시 해당 화면으로 자동으로 넘어오며, 이후 키 입력을 통해 게임 타이틀화면으로 돌아갑니다.

***


### 필요한 기술

* 다른 과목에서 배운 기술: 2d스프라이트 제작 기술, 파이썬 코딩

* 이 과목에서 배울 것으로 기대되는 기술: 키 입력으로 플레이어를 움직이는 기술, 특정 키 입력시 공격 가능한 오브젝트를 쏘아내는 기술, 애니메이션, 충돌 감지, 알파 블렌딩, 사운드, 스프라이트 관련, 스테이트 전환(게임씬 전환)