from flask import Blueprint, render_template

api_Error = Blueprint("Errors", __name__)


@api_Error.errorhandler(400)
def error_400(error):
    return render_template("error/400.html")


@api_Error.errorhandler(404)
def error_404(error):
    """404錯誤處理"""
    return render_template("error/404.html")


@api_Error.errorhandler(500)
def error_500(error):
    """500錯誤處理"""
    return render_template("error/500.html")
