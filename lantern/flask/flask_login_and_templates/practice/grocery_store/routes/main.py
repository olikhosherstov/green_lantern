from flask import Blueprint, render_template
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           user=current_user.name,
                           email=current_user.email,
                           stores=current_user.manage_stores)


@main.route('/orders')
@login_required
def orders():
    orders_list = []
    for order in current_user.orders:
       # import pdb; pdb.set_trace()
        order_data = {"store": order.store.name,
                      "order_date": order.created_time,
                      "order_price": sum([good.good.price for good in order.order_lines]),
                      "order_goods": {good.good.name: good.good.price for good in order.order_lines}
                      }
        orders_list.append(order_data)
    return render_template('orders.html', orders=orders_list)
