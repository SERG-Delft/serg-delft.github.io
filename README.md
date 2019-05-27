## The SERG website

The SERG web site is built with Jekyll and is running on GitHub pages.

### Organization

The website is organized in six top level sections:

* [People](people.md) SERG member profiles
* [Publications](publications.md) Auto-generated publication list
* [Research](research.md) Brief description and links to research lines; list
of open projects.
* [Teaching](teaching.md) Links to our courses
* [MSc projects](msc-projects.md) Open research topics and previous master
  theses.
* [Vacancies](vacancies.md) Open vacancies

### Adding material

Material can be added by anyone in any section. We hereby provide some
templates to make the look and feel more consistent.

#### Adding yourself to People

To add yourself to the People page, copy and modify accordingly the following code snippet. We maintain alphabetic order on the surname.

```html
<div class="card d-block">
    <!--
      Use your GitHub profile picture to avoid duplication. If not available,
      create a 200x200px picture under /img and link it here.
    -->
    <img class="card-img-top" src="https://avatars2.githubusercontent.com/u/220701?v=4" alt="Arie van Deursen">
    <div class="card-body">
      <div class="card-title">
        <!-- Your name, with a link to your website, if exists -->
        <a href="https://avandeursen.com" title="Arie's home page">Arie van Deursen</a>
      </div>
      <!-- Your research interests -->
      <p class="card-text">Group Leader, Software Technology Department Head</p>
    </div>
    <!-- Links to other websites containing your content-->
    <div class="card-footer bg-transparent border-success">
      <a href="https://avandeursen.com" title="Home page"><i class="fas fa-home"></i></a>
      <a href="https://twitter.com/avandeursen" title="Twitter"><i class="fab fa-twitter"></i></a>
      <a href="https://github.com/avandeursen" title="GitHub"><i class="fab fa-github"></i></a>
      <a href="https://nl.linkedin.com/in/avandeursen" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
      <a href="https://scholar.google.nl/citations?user=jjCkWXgAAAAJ" title="Google Scholar"><i class="ai ai-google-scholar-square"></i></a>
      <a href="https://pure.tudelft.nl/portal/en/persons/a-van-deursen(949eb2cc-4db0-4f33-bd56-13425fa5c24a)/publications.html?pageSize=all&page=0" title="Publications"><i class="fas fa-edit"></i></a>
    </div>
  </div>
```

#### Adding master thesis topics

### Building locally

There are two options to build the website locally:

* Installing and running Jekyll
* Running Jekyll from a Docker container

#### Installing and running Jekyll

Jekyll requires Ruby (>=2.3). If you have Ruby installed (most recent Linuxes
and Macs do have a correct version of Ruby), you can use the following commands
to build the web site:

```shell
# Install dependencies
gem install bundler
bundle install

# Build the web site
bundle exec jekyll build

# Run jekyll as web server.
# Automatically rebuilds after a file change
bundle exec jekyll serve
```

#### Running with Docker

You can use Docker to avoid installing Ruby and/or gems. More instructions
[here](https://github.com/envygeeks/jekyll-docker/blob/master/README.md)

```shell
export JEKYLL_VERSION=3.8.4

# Build the web site
docker run --rm --volume="$PWD:/srv/jekyll" -it jekyll/builder:$JEKYLL_VERSION jekyll build

# (Different terminal) Run a local webserver to see the site contents
cd _site
python -m SimpleHTTPServer 4000
```
