require 'test_helper'

class UsersControllerTest < ActionController::TestCase
  test "should get name:string" do
    get :name:string
    assert_response :success
  end

  test "should get password:" do
    get :password:
    assert_response :success
  end

  test "should get string" do
    get :string
    assert_response :success
  end

  test "should get karma:integer" do
    get :karma:integer
    assert_response :success
  end

end
