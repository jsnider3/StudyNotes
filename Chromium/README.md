# Chromium

## How to download and make

mkdir chromium
cd chromium
fetch --nohooks --no-history chromium
git rebase-update
gclient sync
gclient runhooks
cd src
./build/install-build-deps.sh
gn gen out/Default
ninja -C out/Default chrome

# I had to install libgcrypt manually

## How to run

out/Default/chrome
