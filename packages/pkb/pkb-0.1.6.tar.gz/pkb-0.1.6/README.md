# Personal Knowledge Base
Organize personal information with markdown files, folders and search


# Prerequisites
- Python >=3.12.7


# Installation 
Create a knowledge base folder, eg. kb

<pre>
mkdir kb && cd kb
</pre>

Get content folder and .env file for customization later

<pre>
git clone https://github.com/hyw208/pkb.git
cp -R ./pkb/content .
cp .env .
</pre>

Create/activate virtual environment and install pkb lib

<pre>
python -m venv .venv
source .venv/bin/activate
pip install pkb
</pre>
   

# Launch 
<pre>
python -m pkb.fast

// Or

uvicorn pkb.fast:app
</pre>


# Customize
Change site name by editing .env file, save and restart

<pre>
WEBSITE_NAME="Change it"
</pre>

Change navigation items by editing .env file, save and restart,  
<pre>
// from

HEADER_ITEMS=home,services,contact,about,search

// to 

HEADER_ITEMS=home,"new file 1",new_file_2,search
</pre>

ps. make sure to create files "new file 1.md" and "new_file_2.md" with some texts under 'content' folder


# What's next? 
Delete all files you don't need and start create your personal content and have fun~






