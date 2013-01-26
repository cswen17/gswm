class User < ActiveRecord::Base
  attr_accessible :name
#has_secure_password

  before_save :create_remember_token

  validates :name, presence: true, length: { maximum: 50 }
  VALID_EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
  validates :password, presence: true, length: { minimum: 6 }
  validates :password_confirmation, presence: true

  private
    def create_remember_token
        self.remember_token = SecureRandom.urlsafe_base64
    end

end
