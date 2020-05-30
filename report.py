import matplotlib.pyplot as plt
import numpy as np

from fpdf import FPDF

list_of_report_object = []
list_of_report_name = []


class Report:
    def __init__(self):
        self.name = None
        self.header_table = None
        self.body_table = None
        self.discipline = None
        self.group_number = None
        self.period = None
        self.student = None
        self.session = None
        self.type_analysis = None

    def make_report(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('DejaVu', '', 'font/DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 14)
        pdf.cell(200, 10, txt="Отчет", ln=1, align="C")
        pdf.cell(0, 5, '', ln=2)
        pdf.set_font('DejaVu', '', 12)
        pdf.cell(0, 5, 'Тип анализа: ' + self.type_analysis, ln=1)
        pdf.cell(0, 5, '', ln=1)
        y_bar = 40
        if self.group_number is not None:
            pdf.cell(0, 5, 'Группа: ' + self.group_number, ln=1)
            pdf.cell(0, 5, '', ln=1)
            y_bar += 10
        if self.discipline is not None:
            pdf.cell(0, 5, 'Дисциплина: ' + self.discipline, ln=1)
            pdf.cell(0, 5, '', ln=1)
            y_bar += 10
        if self.period is not None:
            pdf.cell(0, 5, 'Период: ' + self.period, ln=1)
            pdf.cell(0, 5, '', ln=1)
            y_bar += 10
        if self.student is not None:
            pdf.cell(0, 5, 'Студент: ' + self.student, ln=1)
            pdf.cell(0, 5, '', ln=1)
            y_bar += 10
        if self.session is not None:
            pdf.cell(0, 5, 'Сессия: ' + self.session, ln=1)
            pdf.cell(0, 5, '', ln=1)
            y_bar += 10

        col_width = pdf.w / 3
        row_height = pdf.font_size
        spacing = 2

        pdf.set_font('DejaVu', '', 14)
        for item in self.header_table:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)
        y_bar += 10

        pdf.set_font('DejaVu', '', 12)
        for row in self.body_table:
            for item in row:
                pdf.cell(col_width, row_height * spacing,
                         txt=item, border=1)
            pdf.ln(row_height * spacing)
            y_bar += 10

        name = []
        value = []
        for i in self.body_table:
            name.append(str(i[0]))
            value.append(float(i[1]))

        x_len = len(self.body_table)
        x = np.arange(0, x_len)

        fig, ax = plt.subplots()
        ax.bar(x, value)
        ax.set_ylabel(self.header_table[1])
        ax.set_xlabel(self.header_table[0])
        ax.set_xticks(x)
        ax.set_xticklabels(name)

        for rect in ax.patches:
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            space = spacing
            va = 'bottom'

            if y_value < 0:
                space *= -1
                va = 'top'

            label = "{:.1f}".format(y_value)

            ax.annotate(
                label,
                (x_value, y_value),
                xytext=(0, space),
                textcoords="offset points",
                ha='center',
                va=va)

        fig.tight_layout()
        image_path = 'temp/bar.png'
        plt.savefig(image_path)

       #  pdf.add_page()
        pdf.cell(0, 5, '', ln=1)
        pdf.cell(0, 5, 'Столбчатая диаграмма:', ln=1)
        pdf.cell(0, 5, '', ln=1)
        pdf.image(image_path, x=7, y=y_bar, w=150)

        """
        plt.pie(value,  # Значения сколько раз встречается определенная степень образования
               labels=name,  # title для частей
               shadow=1,  # Тень
               startangle=90,  # Угол с которого будет начинаться первая доля
               autopct='%1.1f%%'  # Указываем, что необходимо отобраджать проценты
               )
        image_path = 'temp/pie.png'

        plt.savefig(image_path)

        pdf.add_page()
        pdf.cell(0, 5, 'Круговая диаграмма:', ln=1)
        pdf.cell(0, 5, '', ln=1)
        pdf.image(image_path, x=70, y=8, w=100)
        """
        pdf.output("simple_demo.pdf")

