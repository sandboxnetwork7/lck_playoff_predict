# 🏆 LCK 플레이오프 예측기

2025 LCK Champions Korea 플레이오프 토너먼트의 승자를 예측하는 웹 애플리케이션입니다.

## 📁 프로젝트 구조

```
lck-playoff-predictor/
├── app.py              # 메인 Streamlit 앱
├── requirements.txt    # 의존성 파일
├── README.md          # 프로젝트 설명
├── .gitignore         # Git 무시 파일
└── logo/              # 팀 로고 폴더
    ├── t1.svg         # T1 로고
    ├── dk.svg         # DK 로고
    ├── kt.svg         # KT 로고
    ├── bnk.webp       # BFX 로고
    ├── geng.svg       # GEN 로고
    └── hle.svg        # HLE 로고
```

## ✨ 새로운 기능

- **📸 팀 로고 표시**: 각 팀의 공식 로고가 표시됩니다
- **🎨 시각적 UI**: 로고와 함께하는 직관적인 버튼 선택
- **📱 반응형 디자인**: 모바일과 데스크톱 모두 최적화
- **🎭 그라디언트 디자인**: 모던한 색상과 스타일링
- **👀 실시간 미리보기**: 사이드바에서 현재까지 예측 확인

## 📋 기능

- 더블 엘리미네이션 토너먼트 구조
- 11개 단계별 매치 예측
- GEN의 상대 선택권 포함
- 정규리그 순위 기반 패자조 배치
- 직관적인 웹 UI 제공
- 실시간 예측 결과 확인

## 🎮 참가 팀

- **GEN** (1위) - Gen.G
- **HLE** (2위) - Hanwha Life Esports  
- **T1** (3위) - T1
- **KT** (4위) - KT Rolster
- **DK** (5위) - DWG KIA
- **BFX** (6위) - BNK FearX

## 🗓️ 토너먼트 일정

- **R1 M1** (9/10): T1 vs DK
- **R1 M2** (9/11): KT vs BFX
- **R2 M1** (9/13): GEN vs [GEN 선택팀]
- **R2 M2** (9/14): HLE vs [나머지팀]
- **R1 LB** (9/17): R1 패자들 경기
- **R2 LB** (9/18): 패자조 경기
- **R3 UB** (9/20): 승자조 준결승
- **R3 LB** (9/21): 패자조 경기
- **R4 LF** (9/27): 결승진출전
- **Grand Final** (9/28): 최종 결승

## 🚀 실행 방법

### 로컬 실행
```bash
# 저장소 클론
git clone https://github.com/sandboxnetwork7/lck_playoff_predict.git
cd lck-playoff-predict

# 의존성 설치
pip install streamlit

# 앱 실행
streamlit run app.py
```

### 온라인 배포
Streamlit Cloud에서 바로 사용 가능합니다.

## 🎨 로고 파일 요구사항

팀 로고는 다음 형식으로 `logo/` 폴더에 저장해야 합니다:

- **T1**: `t1.svg`
- **DK**: `dk.svg` 
- **KT**: `kt.svg`
- **BFX**: `bnk.svg`
- **GEN**: `geng.svg`
- **HLE**: `hle.svg`

## 📊 토너먼트 규칙

1. **더블 엘리미네이션**: 두 번 져야 탈락
2. **GEN 선택권**: 1위 시드인 GEN이 R1 승자 중 상대 선택
3. **순위별 패자조 배치**: 정규리그 순위가 높을수록 패자조 늦은 진입

## 💻 기술 스택

- **Frontend**: Streamlit
- **Language**: Python 3.8+
- **Styling**: Custom CSS with gradients
- **Icons**: Team logos (SVG/PNG/WEBP)
- **Deployment**: Streamlit Cloud

## 📝 사용법

1. 각 경기마다 팀 로고를 확인하고 승리할 팀의 버튼 클릭
2. 프로그레스 바로 진행상황 확인
3. 사이드바에서 현재까지 예측 확인
4. 최종 결과를 코드 형태로 출력
5. 언제든지 다시 시작 가능

## 🎯 UI 특징

- **로고 중심 디자인**: 각 팀의 로고가 명확히 표시
- **VS 레이아웃**: 직관적인 대결 구조
- **그라디언트 배경**: 모던한 색상 조합
- **반응형 컬럼**: 화면 크기에 따라 자동 조정
- **프로그레스 추적**: 현재 진행 상황 실시간 표시

## 🤝 기여

버그 리포트나 기능 제안은 Issues를 통해 알려주세요!

## 📄 라이선스

MIT License

---

**Made with ❤️ for LCK fans**

🎮 **롤드컵보다 더 치열한 LCK 플레이오프를 예측해보세요!** 🏆