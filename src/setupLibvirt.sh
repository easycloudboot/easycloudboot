yum install -y meson
yum install -y gcc
yum install qemu-kvm

yum install -y libxslt rpcbind

wget https://libvirt.org/sources/libvirt-7.5.0.tar.xz
mkdir -p ~/libvirt
tar xvJf libvirt-7.5.0.tar.xz -C ~/libvirt
cd ~/libvirt/libvirt-7.5.0/

meson build --prefix=/usr
ninja -C build
sudo ninja -C build install