class SessionsController < ApplicationController

  def new
  end

  def create
  user = User.find_by_name()
  if user && user.authenticate()
    sign_in user
  else
      flash.now[:error] = 'Invalid username/password combination'
      render 'new'
  end
  end

  def destroy
  end

end
