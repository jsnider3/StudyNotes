sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo add-apt-repository -y ppa:ethereum/ethereum-dev
sudo apt-get update
sudo apt-get install ethereum

## Make accounts and show them
#mkdir ~/ethchain
#geth -datadir "~/ethchain" -dev account new
#geth -datadir "~/ethchain" -dev account new
#geth account list --keystore ~/ethchain/keystore

## Create private blockchain.
#geth -datadir ~/ethchain/ -unlock 0,1 -mine -minerthreads 2 -rpc -rpcaddr 0.0.0.0 -rpccorsdomain "*" -rpcport 8101 init "/home/josh/Documents/Git/StudyNotes/Blockchain/genesis.json"
#geth -datadir ~/ethchain -unlock 0,1 -mine -minerthreads 2 -rpc -rpcaddr 0.0.0.0 -rpccorsdomain "*" -rpcport 8101
#geth -datadir ~/ethchain attach ipc:/home/josh/ethchain/geth.ipc
