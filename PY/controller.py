
import model_mult as m
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    m.init(value_a,value_b)
    result = m.do_it()
    view.view_data('result',result)