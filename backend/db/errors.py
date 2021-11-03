class UserNotFound( Exception ):
  def __init__( self ):
    self.status_code = "400"
    self.custom_code = "00"
    self.name = "USER_NOT_FOUND"
    self.description = "找不到相對應的使用者。"\
    
    super().__init__( f"{ self.name }: { self.description }" )

class PasswordIncorrect( Exception ):
  def __init__( self ):
    self.status_code = "400"
    self.custom_code = "01"
    self.name = "PASSWORD_INCORRECT"
    self.description = "密碼錯誤，請重新輸入。"
    
    super().__init__( f"{ self.name }: { self.description }" )

class TokenExpired( Exception ):
  def __init__( self ):
    self.status_code = "401"
    self.custom_code = "02"
    self.name = "TOKEN_EXPIRED"
    self.description = "用戶驗證碼已過期。"
    
    super().__init__( f"{ self.name }: { self.description }" )

class TokenUpdateRequired( Exception ):
  def __init__( self ):
    self.status_code = "401"
    self.custom_code = "03"
    self.name = "TOKEN_UPDATE_REQUIRED"
    self.description = "此動作需要更新驗證碼之後才能執行。"
    
    super().__init__( f"{ self.name }: { self.description }" )

class TokenInvalid( Exception ):
  def __init__( self ):
    self.status_code = "401"
    self.custom_code = "03"
    self.name = "TOKEN_INVALID"
    self.description = "驗證代碼出現不知錯誤。"
    
    super().__init__( f"{ self.name }: { self.description }" )