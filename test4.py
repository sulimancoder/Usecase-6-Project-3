import pandas as pd
import streamlit as st
import plotly.express as px
# Load data
apartment =  pd.read_csv("Data/cleaned_Riyadh_Aqqar_Apartments(1).csv")
Realestate = pd.read_csv("Data/cleaned_Real_Estate.csv")
Riyadh_Aqqar_Villas = pd.read_csv("Data/cleaned_Riyadh_Aqqar_Villas.csv")
Riyadh_Aqqar_Land = pd.read_csv("Data/cleaned_Riyadh_Aqqar_Land.csv")
def load_css(theme):
    """Load custom CSS with colors defined by the chosen theme."""
    custom_css = f"""
    <style>
        .stApp {{
            background: {theme['background']};
            text-align: right;
            direction: rtl;
            color: {theme['text_color']};
        }}
        h1, h2, h3 {{
            font-family: {theme['header_font']};
            color: {theme['text_color']};
        }}
        /* Hero Section Styling */
        .hero {{
            background: linear-gradient({theme['hero_overlay']}, {theme['hero_overlay']}), 
                        url('https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf') center/cover;
            padding: 4rem 2rem;
            border-radius: 30px;
            margin: 2rem 0;
        }}
        /* Price Card Styling */
        .price-card {{
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-right: 5px solid;
            color: {theme['text_color']};
        }}
        .price-card.apartment {{ border-color: {theme['accent1']}; }}
        .price-card.villa {{ border-color: {theme['accent2']}; }}
        .price-card.land {{ border-color: {theme['accent3']}; }}
        /* Comparison Box Styling */
        .comparison-box {{
            background: linear-gradient(135deg, #ffffff 0%, {theme['background']} 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid #e9ecef;
        }}
        /* Recommendation Box Styling */
        .recommendation-box {{
            background: {theme['recommendation_bg']};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
        }}
        /* Example Section Styling */
        .example-section {{
            margin-top: 3rem;
            font-size: 1.8rem;
            line-height: 1.7;
        }}
        .example-section h2 {{
            font-size: 2.4rem;
            margin-bottom: 1rem;
            color: {theme['text_color']};
        }}
        .highlight {{
            font-weight: bold;
            color: {theme['accent1']};
            font-size: 1.9rem;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def hero_section(theme):
    """Display the hero section with background image and title."""
    hero_html = f"""
    <div class="hero">
        <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            🏡 رحلة البحث عن منزل في الرياض
        </h1>
        <h3 style="color: white;">اكتشف الخيارات المتاحة ضمن ميزانيتك</h3>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)


def info_sections():
    """Show information sections explaining the choices and add dummy graph images."""
    st.title('رحلة البحث عن منزل في الرياض')

    st.html("""<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>بحث عن منزل في الرياض</title>
  <style>
    body {
      font-size: 24px;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  <p>
    <h1>
    عند البحث عن منزل في الرياض، 🏠<h1>
    قد تجد نفسك أمام حيرة كبيرة بسبب الخيارات المتنوعة والأسعار المتفاوتة. 💸<h1>
    أحيانًا قد تجد نفسك أمام خيار غريب 🤔 هل تختار شقة في حي راقٍ ولكنها ضيقة بعض الشيء؟<h1>
    أم تفضل الانتقال إلى فيلا في حي آخر، مع العلم أن السعر قد يكون مشابهًا بل وربما أقل؟
  </p>
</body>
</html>
""")
    fig = px.scatter_map(Realestate, lat="latitude", lon="longitude", hover_name="district",
                         hover_data=["beds", "price", "furnished", "wc"],
                         color_discrete_sequence=["green"], zoom=8.5, height=500)
    fig.update_layout(map_style="streets")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig, use_container_width=True)
    st.html("""<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>بحث عن منزل في الرياض</title>
  <style>
    body {
      font-size: 24px;
      line-height: 1.5;
    }
  </style>
</head>
<body>
 <h1> سُليمان يبحث عن منزل في الرياض و ميزانيته من 900 الف الى 1100000 امامه عدة خيارات اما شقة او فيلا  او أرض 
هذه الخيارات المتاحة لسُليمان.
</body>
</html>
""")

def price_comparison_section(theme):
    """Render the price comparison cards for different property types.
       The apartment card now displays a Plotly bar chart instead of a dummy image.
    """
    st.markdown("# 🏘️ مقارنة بين الخيارات المتاحة")
    # For the Apartment card, replace the dummy image with a Plotly graph.
    with st.container():
        st.markdown(f"""
        <div class="price-card apartment">
            <h1>الشقق 🏢</h1>
            <h1 style="color: {theme['accent1']};">من900,000 ر.س الى 1,100,000</h1>
        </div>
        """, unsafe_allow_html=True)

        # Create and display the Plotly bar chart using the apartment DataFrame.
        apar = apartment[(apartment["price"] > 900000)]
        cc = apar[(apar["price"] < 1100000)]
        fig3 = px.bar(
            cc,
            x='neighbourhood',
            color="neighbourhood",
            title='عدد الشقق التي تتراوح اسعارها بين (900K) و (1.1M)',
            labels={'neighbourhood': 'الحي', 'price': 'السعر الإجمالي'}
        )
        fig3.update_layout(width=1000, height=900)
        fig3.update_layout(
            title="عدد الشقق التي تتراوح اسعارها بين \u200E(900K)\u200E و \u200E(1.1M)\u200E"
        )

        fig3.update_layout(
            width=1000,
            height=900,
            title_font=dict(size=28),  # Title font size
            xaxis=dict(
                title_font=dict(size=28),  # X-axis title font size
                tickfont=dict(size=28)  # X-axis tick font size
            ),
            yaxis=dict(
                title_font=dict(size=28),  # Y-axis title font size
                tickfont=dict(size=28)  # Y-axis tick font size
            )
        )
        st.plotly_chart(fig3, use_container_width=True)

    # For the Villa and Land cards, we still use the dummy image.

    with st.container():
        st.markdown(f"""
        <div class="price-card villa">
            <h1>الفلل 🏠</h1>
            <h1 style="color: {theme['accent2']};">من900,000 ر.س الى 1,100,000</h1>

        </div>
        """, unsafe_allow_html=True)
        aa = Riyadh_Aqqar_Villas[(Riyadh_Aqqar_Villas["السعر الاجمالي"] > 900000)]
        new_aa = aa[(aa["السعر الاجمالي"] < 1100000)]
        fig1 = px.bar(
            new_aa,
            x='الحي',
            title='عدد الشقق التي تتراوح اسعارها بين 900000 و 1100000',
            labels={'الحي': 'الحي', 'السعر الاجمالي': 'السعر الإجمالي'}
        )
        fig1.update_layout(width=1000, height=900)
        fig1.update_layout(
            width=1000,
            height=900,
            title_font=dict(size=28),  # Title font size
            xaxis=dict(
                title_font=dict(size=28),  # X-axis title font size
                tickfont=dict(size=28)  # X-axis tick font size
            ),
            yaxis=dict(
                title_font=dict(size=28),  # Y-axis title font size
                tickfont=dict(size=28)  # Y-axis tick font size
            )
        )
        st.plotly_chart(fig1, use_container_width=True)


    with st.container():
            st.markdown(f"""
            <div class="price-card land">
                <h1>الأراضي  🏜️</h1>
                <h1 style="color: {theme['accent3']};">من900,000 ر.س الى 1,100,000</h1>
            </div>
            """, unsafe_allow_html=True)
            average_price_per_district = Riyadh_Aqqar_Land.groupby("الحي")["سعر المتر"].mean().reset_index().head(10)
            fig2 = px.bar(
                average_price_per_district,
                x='الحي',
                y='سعر المتر',
                color="الحي",
                title="متوسط سعر المتر في احياء الرياض ",
                labels={'الحي': 'الحي', 'السعر الاجمالي': 'السعر الإجمالي'}
            )
            fig2.update_layout(width=1000, height=900)
            fig2.update_layout(
                width=1000,
                height=900,
                title_font=dict(size=28),  # Title font size
                xaxis=dict(
                    title_font=dict(size=28),  # X-axis title font size
                    tickfont=dict(size=28)  # X-axis tick font size
                ),
                yaxis=dict(
                    title_font=dict(size=28),  # Y-axis title font size
                    tickfont=dict(size=28)  # Y-axis tick font size
                )
            )
            st.plotly_chart(fig2, use_container_width=True)





def recommendation_section(theme):
    """Display recommendations and tips for decision making with enhanced text size."""

    st.html("""<!DOCTYPE html>
    <html lang="ar">
    <head>
      <meta charset="UTF-8">
      <title>بحث عن منزل في الرياض</title>
      <style>
        body {
          font-size: 24px;
          line-height: 1.5;
        }
      </style>
    </head>
    <body>
     <h1> في النهاية، قرار سليمان يعتمد على أولوياته واحتياجاته. هل يفضل المساحة الأكبر والخصوصية التي توفرها الفيلا؟ أم يفضل الموقع الراقي والخدمات المتاحة في الشقة؟ وربما يفكر في شراء أرض وبناء منزله المستقبلي وفقًا لرؤيته الخاصة. مهما كان خياره، الأهم أن يجد المكان الذي يشعر فيه بالراحة والاستقرار. 
    </body>
    </html>
    """)
    st.markdown(f"""
    <div class="recommendation-box" style="font-size: 2rem; padding: 2rem;">
        <h2 style="font-size: 3rem; margin-bottom: 1rem;">💡 نصائح لاتخاذ القرار</h2>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
            <div style="border-left: 3px solid {theme['accent1']}; padding-left: 1rem;">
                <h3 style="font-size: 2.2rem; margin-bottom: 0.5rem;">العوامل المهمة:</h3>
                <p style="font-size: 2rem; line-height: 1.5; margin: 0;">
                    <strong>✓ قرب الخدمات الأساسية</strong><br>
                    <strong>✓ جودة البناء</strong><br>
                    <strong>✓ مستقبل المنطقة</strong>
                </p>
            </div>
            <div style="border-left: 3px solid {theme['accent2']}; padding-left: 1rem;">
                <h3 style="font-size: 2.2rem; margin-bottom: 0.5rem;">التوصيات:</h3>
                <p style="font-size: 2rem; line-height: 1.5; margin: 0;">
                    <strong>✓ زيارة الموقع شخصيًا</strong><br>
                    <strong>✓ دراسة خيار التمويل</strong><br>
                    <strong>✓ مقارنة عروض مختلفة</strong>
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



def main():
    st.set_page_config(layout="wide", page_title="رحلة البحث عن منزل")

    # Pastel theme configuration
    pastel_theme = {
        "background": "#fdf6e3",
        "text_color": "#657b83",
        "accent1": "#b58900",
        "accent2": "#cb4b16",
        "accent3": "#268bd2",
        "hero_overlay": "rgba(38, 139, 210, 0.4)",
        "header_font": "'Tajawal', sans-serif",
        "recommendation_bg": "#657b83",
    }

    theme = pastel_theme

    load_css(theme)
    hero_section(theme)
    info_sections()
    price_comparison_section(theme)
    recommendation_section(theme)


if __name__ == "__main__":
    main()  
