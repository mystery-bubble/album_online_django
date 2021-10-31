from logging import log
from flask import Blueprint, render_template

error_tem = Blueprint("Errors", __name__)


@error_tem.errorhandler(400)
def error_400(error):
    return render_template("error/400.html")


@error_tem.errorhandler(404)
def error_404(error):
    """404錯誤處理"""
    print(error)
    return render_template("error/404.html")


@error_tem.errorhandler(500)
def error_500(error):
    """500錯誤處理"""
    return render_template("error/500.html")
