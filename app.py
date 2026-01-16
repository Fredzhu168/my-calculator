import streamlit as st

# 设置网页标题
st.title("📊 培训机构财务计算器")
st.subheader("输入各项参数，实时查看利润分析")

# 在侧边栏设置输入参数
with st.sidebar:
    st.header("参数设置")
    students_count = st.number_input("学生人数", min_value=1, value=10)
    price_per_student = st.number_input("单价（元/人）", min_value=0, value=100)
    hours = st.slider("课时数量", 1, 10, 2)
    teacher_fee_per_hour = st.number_input("老师时薪", min_value=0, value=150)
    transport_subsidy = st.number_input("交通补贴", min_value=0, value=50)

# 计算核心逻辑
total_revenue = students_count * price_per_student * hours
total_cost = (teacher_fee_per_hour * hours) + transport_subsidy
profit = total_revenue - total_cost
cost_ratio = (total_cost / total_revenue) * 100 if total_revenue > 0 else 0

# 在网页主界面显示结果
col1, col2, col3 = st.columns(3)
col1.metric("总收入", f"¥{total_revenue}")
col2.metric("总成本", f"¥{total_cost}")
col3.metric("净利润", f"¥{profit}", delta=f"{profit}")

# 进度条展示成本占比
st.write(f"**成本占比：{cost_ratio:.1f}%**")
st.progress(min(cost_ratio / 100, 1.0))

if profit > 0:
    st.success("💰 这一单是盈利的！")
else:
    st.error("⚠️ 注意：这一单亏损了，请调整参数。")
