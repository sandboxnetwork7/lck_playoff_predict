import streamlit as st
import os

def load_team_logo(team_name):
    """팀 로고 파일 경로를 반환합니다."""
    logo_mapping = {
        "T1": "t1.svg",
        "DK": "dk.svg", 
        "KT": "kt.svg",
        "BFX": "bnk.svg",
        "GEN": "geng.svg",
        "HLE": "hle.svg"
    }
    
    logo_file = logo_mapping.get(team_name)
    if logo_file and os.path.exists(f"logo/{logo_file}"):
        return f"logo/{logo_file}"
    return None

def display_team_vs_ui(team1, team2, match_title, match_info="", key_prefix=""):
    """두 팀의 대결 UI를 표시합니다."""
    st.subheader(match_title)
    if match_info:
        st.caption(match_info)
    
    # 팀 로고와 버튼 레이아웃
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        # 팀1 로고 (높이 통일)
        logo1 = load_team_logo(team1)
        if logo1:
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 120px;">
                <img src="data:image/svg+xml;base64,{get_base64_image(logo1)}" style="max-height: 100px; max-width: 120px; object-fit: contain;">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: center; font-size: 48px; padding: 20px; height: 120px; display: flex; align-items: center; justify-content: center;'>🏆</div>", unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='text-align: center;'>{team1}</h3>", unsafe_allow_html=True)
        
        # 팀1 선택 버튼
        if st.button(f"{team1} 승리", key=f"{key_prefix}_{team1}", use_container_width=True, type="primary"):
            return team1
    
    with col2:
        st.markdown("<div style='text-align: center; font-size: 24px; padding: 40px 0;'>VS</div>", unsafe_allow_html=True)
    
    with col3:
        # 팀2 로고 (높이 통일)
        logo2 = load_team_logo(team2)
        if logo2:
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 120px;">
                <img src="data:image/svg+xml;base64,{get_base64_image(logo2)}" style="max-height: 100px; max-width: 120px; object-fit: contain;">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: center; font-size: 48px; padding: 20px; height: 120px; display: flex; align-items: center; justify-content: center;'>🏆</div>", unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='text-align: center;'>{team2}</h3>", unsafe_allow_html=True)
        
        # 팀2 선택 버튼
        if st.button(f"{team2} 승리", key=f"{key_prefix}_{team2}", use_container_width=True, type="primary"):
            return team2
    
    return None

def display_team_selection_ui(teams, title, subtitle="", key_prefix=""):
    """여러 팀 중에서 선택하는 UI를 표시합니다."""
    st.subheader(title)
    if subtitle:
        st.write(subtitle)
    
    # 팀 수에 따라 컬럼 조정
    if len(teams) == 2:
        cols = st.columns(2)
    else:
        cols = st.columns(len(teams))
    
    for i, team in enumerate(teams):
        with cols[i]:
            # 팀 로고 (높이 통일)
            logo = load_team_logo(team)
            if logo:
                st.markdown(f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
                    <img src="data:image/svg+xml;base64,{get_base64_image(logo)}" style="max-height: 80px; max-width: 100px; object-fit: contain;">
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: center; font-size: 36px; padding: 10px; height: 100px; display: flex; align-items: center; justify-content: center;'>🏆</div>", unsafe_allow_html=True)
            
            st.markdown(f"<h4 style='text-align: center;'>{team}</h4>", unsafe_allow_html=True)
            
            # 선택 버튼
            if st.button(f"{team} 선택", key=f"{key_prefix}_{team}", use_container_width=True):
                return team
    
    return None

def get_base64_image(image_path):
    """이미지를 base64로 인코딩합니다."""
    import base64
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

def create_copy_button(text_to_copy):
    """클립보드 복사 버튼을 생성합니다."""
    button_html = f"""
    <div style="margin: 10px 0;">
        <button onclick="copyToClipboard()" style="
            background-color: #FF6B6B;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        ">📋 클립보드에 복사</button>
    </div>
    <script>
        function copyToClipboard() {{
            const text = `{text_to_copy}`;
            navigator.clipboard.writeText(text).then(function() {{
                alert('클립보드에 복사되었습니다!');
            }}, function(err) {{
                console.error('복사 실패: ', err);
                // 대체 방법
                const textArea = document.createElement("textarea");
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                alert('클립보드에 복사되었습니다!');
            }});
        }}
    </script>
    """
    return button_html

def display_match_result(match_name, team1, team2, winner):
    """매치 결과를 시각적으로 표시합니다."""
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    
    with col1:
        st.write(f"**{match_name}**")
    
    with col2:
        # 팀1 로고
        logo1 = load_team_logo(team1)
        if logo1:
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 30px;">
                <img src="data:image/svg+xml;base64,{get_base64_image(logo1)}" style="max-height: 25px; max-width: 30px; object-fit: contain;">
            </div>
            """, unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 12px; margin: 0;'>{team1}</p>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<p style='text-align: center; margin: 0;'>vs</p>", unsafe_allow_html=True)
    
    with col4:
        # 팀2 로고
        logo2 = load_team_logo(team2)
        if logo2:
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 30px;">
                <img src="data:image/svg+xml;base64,{get_base64_image(logo2)}" style="max-height: 25px; max-width: 30px; object-fit: contain;">
            </div>
            """, unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 12px; margin: 0;'>{team2}</p>", unsafe_allow_html=True)
    
    with col5:
        # 승리팀 로고
        winner_logo = load_team_logo(winner)
        if winner_logo:
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 30px;">
                <img src="data:image/svg+xml;base64,{get_base64_image(winner_logo)}" style="max-height: 25px; max-width: 30px; object-fit: contain;">
            </div>
            """, unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 12px; margin: 0; color: #FF6B6B; font-weight: bold;'>{winner}</p>", unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="2025 LCK 플레이오프 예측기",
        page_icon="🏆",
        layout="wide"
    )
    
    # 커스텀 CSS
    st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #FF6B6B;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .team-ranking {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        color: white;
    }
    .match-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #e9ecef;
    }
    .result-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 제목
    st.markdown('<h1 class="main-title">🏆 2025 LCK 플레이오프 예측기</h1>', unsafe_allow_html=True)
    
    # 정규리그 순위 표시
    st.markdown('<div class="team-ranking">', unsafe_allow_html=True)
    st.subheader("📊 정규리그 순위")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    ranking_teams = ["GEN", "HLE", "T1", "KT", "DK", "BFX"]
    ranking_positions = ["1위", "2위", "3위", "4위", "5위", "6위"]
    
    for i, (col, team, pos) in enumerate(zip([col1, col2, col3, col4, col5, col6], ranking_teams, ranking_positions)):
        with col:
            logo = load_team_logo(team)
            if logo:
                st.markdown(f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 60px;">
                    <img src="data:image/svg+xml;base64,{get_base64_image(logo)}" style="max-height: 40px; max-width: 60px; object-fit: contain;">
                </div>
                """, unsafe_allow_html=True)
            st.metric(pos, team)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 세션 스테이트 초기화
    if 'predictions' not in st.session_state:
        st.session_state.predictions = []
        st.session_state.current_step = 1
        st.session_state.teams_state = {}
        st.session_state.match_details = []  # 매치 세부정보 저장
    
    # 정규리그 순위
    regular_season_ranking = {"GEN": 1, "HLE": 2, "T1": 3, "KT": 4, "DK": 5, "BFX": 6}
    
    # 프로그레스 바
    progress = min(st.session_state.current_step / 11, 1.0)
    st.progress(progress)
    st.markdown(f"<h4 style='text-align: center;'>진행률: {st.session_state.current_step}/12</h4>", unsafe_allow_html=True)
    
    # 현재 단계에 따른 질문 표시
    if st.session_state.current_step == 1:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        winner = display_team_vs_ui("T1", "DK", "1️⃣ R1 M1 (9/10)", key_prefix="r1_m1")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r1_m1_winner'] = winner
            st.session_state.teams_state['r1_m1_loser'] = "DK" if winner == "T1" else "T1"
            st.session_state.match_details.append({"match": "R1 M1", "team1": "T1", "team2": "DK", "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 2:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        winner = display_team_vs_ui("KT", "BFX", "2️⃣ R1 M2 (9/11)", key_prefix="r1_m2")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r1_m2_winner'] = winner
            st.session_state.teams_state['r1_m2_loser'] = "BFX" if winner == "KT" else "KT"
            st.session_state.match_details.append({"match": "R1 M2", "team1": "KT", "team2": "BFX", "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 3:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r1_winners = [st.session_state.teams_state['r1_m1_winner'], st.session_state.teams_state['r1_m2_winner']]
        choice = display_team_selection_ui(
            r1_winners, 
            "3️⃣ GEN의 선택", 
            f"GEN이 상대로 선택할 팀은? (R1 승자: {', '.join(r1_winners)})",
            key_prefix="gen_choice"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if choice:
            st.session_state.predictions.append(choice)
            st.session_state.teams_state['gen_choice'] = choice
            st.session_state.teams_state['hle_opponent'] = r1_winners[1] if choice == r1_winners[0] else r1_winners[0]
            st.session_state.match_details.append({"match": "GEN의 선택", "team1": "-", "team2": "-", "winner": choice})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 4:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        gen_choice = st.session_state.teams_state['gen_choice']
        winner = display_team_vs_ui("GEN", gen_choice, "4️⃣ R2 M1 (9/13)", key_prefix="r2_m1")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r2_m1_winner'] = winner
            st.session_state.teams_state['r2_m1_loser'] = gen_choice if winner == "GEN" else "GEN"
            st.session_state.match_details.append({"match": "R2 M1", "team1": "GEN", "team2": gen_choice, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 5:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        hle_opponent = st.session_state.teams_state['hle_opponent']
        winner = display_team_vs_ui("HLE", hle_opponent, "5️⃣ R2 M2 (9/14)", key_prefix="r2_m2")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r2_m2_winner'] = winner
            st.session_state.teams_state['r2_m2_loser'] = hle_opponent if winner == "HLE" else "HLE"
            st.session_state.match_details.append({"match": "R2 M2", "team1": "HLE", "team2": hle_opponent, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 6:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r1_m1_loser = st.session_state.teams_state['r1_m1_loser']
        r1_m2_loser = st.session_state.teams_state['r1_m2_loser']
        winner = display_team_vs_ui(
            r1_m1_loser, r1_m2_loser, 
            "6️⃣ R1 LB (9/17)", 
            "R1 패자들끼리의 경기",
            key_prefix="r1_lb"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r1_lb_winner'] = winner
            st.session_state.match_details.append({"match": "R1 LB", "team1": r1_m1_loser, "team2": r1_m2_loser, "winner": winner})
            
            # R2 패자들의 순위 결정
            r2_losers = [st.session_state.teams_state['r2_m1_loser'], st.session_state.teams_state['r2_m2_loser']]
            r2_loser_higher_rank = min(r2_losers, key=lambda x: regular_season_ranking[x])
            r2_loser_lower_rank = max(r2_losers, key=lambda x: regular_season_ranking[x])
            st.session_state.teams_state['r2_loser_higher_rank'] = r2_loser_higher_rank
            st.session_state.teams_state['r2_loser_lower_rank'] = r2_loser_lower_rank
            
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 7:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r2_loser_lower_rank = st.session_state.teams_state['r2_loser_lower_rank']
        r1_lb_winner = st.session_state.teams_state['r1_lb_winner']
        r2_m1_loser = st.session_state.teams_state['r2_m1_loser']
        r2_m2_loser = st.session_state.teams_state['r2_m2_loser']
        
        match_info = f"R2 M1, M2 패배팀 {r2_m1_loser}, {r2_m2_loser} 중에서 정규리그 순위가 {r2_loser_lower_rank}팀이 더 낮으므로 {r2_loser_lower_rank}팀으로 배치"
        
        winner = display_team_vs_ui(
            r2_loser_lower_rank, r1_lb_winner,
            "7️⃣ R2 LB (9/18)",
            match_info,
            key_prefix="r2_lb"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r2_lb_winner'] = winner
            st.session_state.match_details.append({"match": "R2 LB", "team1": r2_loser_lower_rank, "team2": r1_lb_winner, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 8:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r2_m1_winner = st.session_state.teams_state['r2_m1_winner']
        r2_m2_winner = st.session_state.teams_state['r2_m2_winner']
        winner = display_team_vs_ui(
            r2_m1_winner, r2_m2_winner,
            "8️⃣ R3 UB (9/20)",
            "R2 승자들끼리의 경기",
            key_prefix="r3_ub"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r3_ub_winner'] = winner
            st.session_state.teams_state['r3_ub_loser'] = r2_m2_winner if winner == r2_m1_winner else r2_m1_winner
            st.session_state.match_details.append({"match": "R3 UB", "team1": r2_m1_winner, "team2": r2_m2_winner, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 9:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r2_loser_higher_rank = st.session_state.teams_state['r2_loser_higher_rank']
        r2_lb_winner = st.session_state.teams_state['r2_lb_winner']
        winner = display_team_vs_ui(
            r2_loser_higher_rank, r2_lb_winner,
            "9️⃣ R3 LB (9/21)",
            "R2 패자 중 순위 높은 팀이 마지막으로 패자조 진입",
            key_prefix="r3_lb"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r3_lb_winner'] = winner
            st.session_state.match_details.append({"match": "R3 LB", "team1": r2_loser_higher_rank, "team2": r2_lb_winner, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 10:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r3_ub_loser = st.session_state.teams_state['r3_ub_loser']
        r3_lb_winner = st.session_state.teams_state['r3_lb_winner']
        winner = display_team_vs_ui(
            r3_ub_loser, r3_lb_winner,
            "🔟 R4 LF (9/27) - 결승진출전",
            "패자조 최종 승자 vs 승자조에서 떨어진 팀",
            key_prefix="r4_lf"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.teams_state['r4_lf_winner'] = winner
            st.session_state.match_details.append({"match": "R4 LF", "team1": r3_ub_loser, "team2": r3_lb_winner, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step == 11:
        st.markdown('<div class="match-container">', unsafe_allow_html=True)
        r3_ub_winner = st.session_state.teams_state['r3_ub_winner']
        r4_lf_winner = st.session_state.teams_state['r4_lf_winner']
        winner = display_team_vs_ui(
            r3_ub_winner, r4_lf_winner,
            "🏆 Grand Final (9/28)",
            "우승을 가려내는 최종 결승전!",
            key_prefix="grand_final"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if winner:
            st.session_state.predictions.append(winner)
            st.session_state.match_details.append({"match": "Grand Final", "team1": r3_ub_winner, "team2": r4_lf_winner, "winner": winner})
            st.session_state.current_step += 1
            st.rerun()
    
    elif st.session_state.current_step > 11:
        # 결과 표시
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.subheader("🎉 예측 완료!")
        st.success("모든 예측이 완료되었습니다!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 예측 결과 도표
        st.subheader("📋 예측 결과")
        st.markdown("---")
        
        for detail in st.session_state.match_details:
            st.markdown('<div class="match-result">', unsafe_allow_html=True)
            if detail["match"] == "GEN의 선택":
                col1, col2 = st.columns([2, 3])
                with col1:
                    st.write(f"**{detail['match']}**")
                with col2:
                    winner_logo = load_team_logo(detail["winner"])
                    col2_1, col2_2 = st.columns([1, 4])
                    with col2_1:
                        if winner_logo:
                            st.markdown(f"""
                            <div style="display: flex; justify-content: center; align-items: center; height: 30px;">
                                <img src="data:image/svg+xml;base64,{get_base64_image(winner_logo)}" style="max-height: 25px; max-width: 30px; object-fit: contain;">
                            </div>
                            """, unsafe_allow_html=True)
                    with col2_2:
                        st.markdown(f"<p style='color: #FF6B6B; font-weight: bold; margin: 0;'>{detail['winner']}</p>", unsafe_allow_html=True)
            else:
                display_match_result(detail["match"], detail["team1"], detail["team2"], detail["winner"])
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 복사용 텍스트
        st.subheader("📝 최종 예측 결과 (복사용)")
        
        result_text = ""
        match_labels = [
            "R1 M1", "R1 M2", "GEN이 고른 팀", "R2 M1", "R2 M2",
            "R1 LB", "R2 LB", "R3 UB", "R3 LB", "R4 LF", "Grand Final"
        ]
        
        for label, prediction in zip(match_labels, st.session_state.predictions):
            result_text += f"{label} : {prediction}\n"
        
        # 복사 버튼
        st.components.v1.html(create_copy_button(result_text), height=60)
        
        # 텍스트 영역
        st.text_area("텍스트 복사", value=result_text, height=300, help="위 버튼을 클릭하거나 텍스트를 직접 복사하세요")
        
        # 우승팀 하이라이트
        champion = st.session_state.predictions[-1]
        st.markdown("### 🏆 예측 우승팀")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            logo = load_team_logo(champion)
            if logo:
                st.markdown(f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
                    <img src="data:image/svg+xml;base64,{get_base64_image(logo)}" style="max-height: 150px; max-width: 200px; object-fit: contain;">
                </div>
                """, unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: gold;'>{champion}</h2>", unsafe_allow_html=True)
        
        # 리셋 버튼
        if st.button("🔄 다시 예측하기", use_container_width=True, type="secondary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # 사이드바에 현재까지의 예측 표시
    if st.session_state.predictions:
        st.sidebar.subheader("🔍 현재까지 예측")
        questions = [
            "R1 M1", "R1 M2", "GEN이 고른 팀", "R2 M1", "R2 M2",
            "R1 LB", "R2 LB", "R3 UB", "R3 LB", "R4 LF", "Grand Final"
        ]
        
        for i, prediction in enumerate(st.session_state.predictions):
            col1, col2 = st.sidebar.columns([1, 3])
            with col1:
                logo = load_team_logo(prediction)
                if logo:
                    st.markdown(f"""
                    <div style="display: flex; justify-content: center; align-items: center; height: 30px;">
                        <img src="data:image/svg+xml;base64,{get_base64_image(logo)}" style="max-height: 20px; max-width: 30px; object-fit: contain;">
                    </div>
                    """, unsafe_allow_html=True)
            with col2:
                st.write(f"{i+1}. **{prediction}**")

if __name__ == "__main__":
    main()