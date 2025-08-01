import grpc
from grpc_interceptor import ServerInterceptor


class IPLoggingInterceptor(ServerInterceptor):
    def intercept(self, method, request, context, method_name):
        # Extract IP address from peer info
        peer = context.peer()  # e.g., "ipv4:127.0.0.1:12345"
        ip_address = "unknown"
        if peer.startswith("ipv4:") or peer.startswith("ipv6:"):
            parts = peer.split(":")
            if len(parts) >= 2:
                ip_address = parts[1]

        print(f"[gRPC] IP: {ip_address} | Method: {method_name}")

        # Call the actual RPC method
        return method(request, context)
