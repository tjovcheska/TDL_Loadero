PATH=$PATH:/Users/teodorajovcheska/.pyenv/bin:/Users/teodorajovcheska/.pyenv/shims:/Users/teodorajovcheska/.pyenv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
echo $PATH
python3 --version
pip3 --version
pip3 install virtualenv
virtualenv --version
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate