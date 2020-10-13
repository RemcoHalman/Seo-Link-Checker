# SEO link status checker


## Installing locally

The project is meant to run in a Docker container so that both the front and backend start and run at the same time. If you want to test it out locally it is a little more complicated to set up.

#### Frontend installation
Open a new terminal window. `cd` to the `Frontend` folder and run the following command

```
npm install
```
On completion and no errors run the next command to compile the project and sets hot-reloads for **development**

```
npm run serve
```

#### Backend installation

Open a new terminal tab and `cd` to the `Backend` folder and run the following commands in order to run the API

```bash
python3 -m venv venv
source /venv/bin/activate
pip install -r ../requirements.txt
python app.py
```





## Project Tree

```bash
.
├── Backend
│   ├── app.py
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   ├── js
│   │   │   └── main.js
│   │   └── scss
│   │       └── main.scss
│   └── views.py
├── Frontend
│   ├── babel.config.js
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   │   ├── GitHub-Mark-32px.png
│   │   │   └── logo.png
│   │   ├── components
│   │   │   ├── Footer.vue
│   │   │   ├── Header.vue
│   │   │   ├── LinkInput.vue
│   │   │   └── LinkStatus.vue
│   │   ├── main.js
│   │   └── mixins
│   │       └── titleMixin.js
│   └── vue.config.js
├── README.md
├── requirements.txt
└── tree.txt

11 directories, 23 files
```
