#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/imu.hpp>

#include <vn/sensors.h>
#include <vn/thread.h>

namespace vn_ros {

class VectorNavNode : public rclcpp::Node {
  public:
    explicit VectorNavNode(const rclcpp::NodeOptions& options);
    ~VectorNavNode();

  private:
    static void vncxx_callback(void* user_data, vn::protocol::uart::Packet& packet, size_t index);
    void        read_imu(vn::protocol::uart::Packet& packet, size_t index);

    vn::sensors::VnSensor sensor_;

    std::string   frame_id_;
    double accelerometer_variance_, gyroscope_variance_;

    rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr publisher_;
    size_t                                              samples_read;
};

} // namespace vn_ros