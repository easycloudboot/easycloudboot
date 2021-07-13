wget https://download.qemu.org/qemu-6.0.0.tar.xz
mkdir -p ~/qemu
tar xvJf qemu-6.0.0.tar.xz -C ~/qemu
cd ~/qemu/qemu-6.0.0
./configure
make -j 40 && make install
