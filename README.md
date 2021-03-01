# Getting with started with dask running with Okteto

## Prepare

First of all, this needs to be the project where you connect to, so make sure you move the files and install the dependencies you need to here.

You can also move those files into your project, in that case, make sure you move the following files

- okteto.yml
- prepare-cluster.yml
- worker-spec.yml
- requirements.txt

**About requirements.txt**

The dependencies and the versions has to be the ones specified in that file, dask requires that the versions of the workers and the master (the one that triggers the scale of the workers) are the same, otherwise it doesn't work properly.

### Install Okteto

https://okteto.com/docs/getting-started/installation/index.html


### Deploy a remote python container into the cluster

This python container is used to okteto connect to, so we can remotely execute our code.

In your console or terminal, run the following

```bash
kubectl apply -f prepare-cluster.yml
```

## Connect to the cluster

In your console or terminal, run the following

```bash
okteto up
```

So now you have a running terminal in the cluster with your code on it.

There is a synchronization service running that moves synchronizes your project folder into `/usr/src/app`, just run `cd /usr/src/app` to make sure you are using those files.

## Running

Install the requirements.txt

```bash
python -m pip install -r requirements.txt
```

Run your code, for example

```bash
python app.py
```
