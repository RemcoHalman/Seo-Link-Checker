# SEO link status checker

## Project installation

open the terminal and navigate to the main folder `seo-link-checker` and run `docker-compose up --build`


## Installing locally

The project is meant to run in a Docker container so that both the front and backend start and run at the same time. If you want to test it out locally it is a little more complicated to set up.

#### Frontend installation (In development)
Open a new terminal window. `cd` to the `Frontend` folder and run the following command

```
npm install
```
On completion and no errors run the next command to compile the project and sets hot-reloads for **development**

```
npm run serve
```

#### Backend installation (MVP)

Open a new terminal tab and `cd` to the `Backend` folder and run the following commands in order to run the API

```bash
python3 -m venv venv
source /venv/bin/activate
pip install -r ../requirements.txt
python app.py
```

### Frontend View

![Frontend](https://user-images.githubusercontent.com/25010775/96105173-071e0780-0eda-11eb-84bf-ce90eee90d45.jpg)

## Project Tree

```bash
.
├── Backend
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── static
│       ├── css
│       │   └── main.css
│       ├── js
│       │   └── main.js
│       └── scss
│           └── main.scss
├── Frontend
│   ├── Dockerfile
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
└── docker-compose.yml

11 directories, 24 files
```
