# Deploy with Deta

Learn to self-host an RSSerpent instance on [deta.sh](https://www.deta.sh/) (for *free*) through this tutorial.

## Access Token

In order to deploy on Deta, you need to create an account at <https://web.deta.sh> first.

After successful registration & sign-in, you will need to create an **access token** so that RSSerpent could help you do the rest!

1. Go to your home page `https://web.deta.sh/home/{username}/`;
2. Click the *Settings* tab, then click the *Create Token* button;
3. Copy the generated access token to your clipboard.

Read Deta's [document](https://docs.deta.sh/docs/cli/auth) if you have any question/concern about the access token.

## Use the Template

RSSerpent provides a Deta deployment template. You will need an [GitHub](https://github.com/) account before continuing.

1. Go to the [template](https://github.com/RSSerpent/rsserpent-deploy-deta) on GitHub;
2. Click the green *Use this template* button.

You will be prompted to create a repository based on the template. After successful creation:

1. Go to your repository's *Settings* tab;
2. Go to the *Secrets* section, click the *New repository secret* button;
3. Create a secret whose name is *DETA_TOKEN* and whose value is the Deta access token you just created.

GitHub will need the access token so that it could automatically deploy your RSSerpent instance on Deta.

## Running 🎉

1. Go to your repository -> *Actions* tab -> *All workflows* -> *Update*, click the *Run workflow* button to manually trigger the first deployment;
2. Go to your [deta.sh](https://www.deta.sh/) home page -> *default* project -> *Micros*, select *rsserpent*, you will see the domain name of your instance (usually *https://xxxxxx.deta.dev/*) at the top-right corner.

Open that domain in your browser. If you see the *"Welcome to RSSerpent!"* message, congratulations, you are good to go!

## Miscellany

If you wish to add RSSerpent plugins, read [Install Plugins](./plugin.md).

If you need a custom domain, read Deta's [document](https://docs.deta.sh/docs/micros/custom_domains).
