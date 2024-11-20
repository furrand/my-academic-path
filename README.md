# My Academic Path

The goal of this project is to empower students to plan their academic
future. We are using data from [Assist.org](https://www.assist.org) to
power an app that allows comparisons of major requirements across multiple
universities.

## Development Guide

To get the project up and running on your personal computer there's a few
steps to take.

First, clone this git repo. The easiest way to do this is to open a terminal,
and `cd` into the directory where you'd like to save the project, then enter
the following command:

```bash
git clone https://github.com/mattag1234/better-assist.git
```

After this, the project will be downloaded to your machine.

Next, you need to build the docker image. To do this, first make sure that
Docker is [installed](https://docs.docker.com/engine/install/) on your computer.

Once you're sure you've got docker installed, open a terminal and `cd` into
the `better-assist` project directory (the one you just cloned).

From inside the directory, type in the command:

```bash
make dev-build
```

This will build the docker image, installing all of the required dependencies
and ensuring that everything runs the same on everyone's computer. The first
time you do this it may take about a minute.

After the image has been built, the final step is to spin up the containers,
this basically means that the application will start running and you can
access it through the browser on your computer. It will reload whenever you
make changes to the code.

To run the containers, run the following command from inside the
`better-assist` directory:

```bash
make dev-up
```

Once this completes, you can view the front-end of the website at
`127.0.0.1:3000`. The backend is running on `127.0.0.1:8000/api`
