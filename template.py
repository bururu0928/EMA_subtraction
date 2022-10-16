from manim import *

#自動調整位置表產生器
def table_gen(a_str_list, b_str_list, ans_str_list, max_len):

    #column標籤
    col_name_ref=[Text('千兆'), Text('百兆'), Text('十兆'), Text('兆'), Text('千億'), Text('百億'), Text('十億'), Text('億'), Text('千萬'), Text('百萬'), Text('十萬'), Text('萬'), Text('千'), Text('百'), Text('十'), Text('個')]
    col_name = col_name_ref[-max_len:]

    #產生位置表
    t0 = Table(
        [a_str_list, b_str_list, ans_str_list],
        row_labels=[Text(" "), Text("-"), Text("=")],
        col_labels = col_name,
        include_outer_lines=True)

    #尺寸調整
    scale_x = (config.frame_width-2)/t0.width
    scale_y = (config.frame_height-5)/t0.height

    t0 = t0.scale(min(scale_x, scale_y)).to_corner(DOWN, buff=1.6)

    #顏色調整
    for i in range(max_len):
            t0.add_highlighted_cell((1,2+i), color=GREEN)
    t0.get_horizontal_lines()[4].set_color(GREEN)
    t0.get_entries_without_labels()[-max_len:].set_color(BLACK)

    return t0