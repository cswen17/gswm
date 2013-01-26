class UsersController < ApplicationController

  def create 
    @user = User.new(params[:user])
    if @user.save
        sign_in @user
        flash[:success] = "Welcome!"
    else
        render 'new'
    end
  end

end
