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
To add yourself to the People page, create a new file in the `_people` directory with the following content:

```markdown
---
given_name:
surname:
interests:
current_affiliation: SERG
role:
start_date:
end_date:

website_url:
email:
github:
linkedin:
google_scholar:
xdotcom:
stackoverflow:
tudelft_research:
researchgate:
mastodon:
speakerdeck:
---
```

Take a look at the existing files in the [`_people`](./_people) directory for examples.

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
docker run --rm -p4000:4000 --volume="$PWD:/srv/jekyll" -it jekyll/builder:$JEKYLL_VERSION jekyll serve
```
