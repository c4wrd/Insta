using System;
using System.Collections.Generic;
using EasyHttp.Http;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Dynamic;
using System.Collections;
using Newtonsoft.Json;
using System.Web;
using RestSharp;

namespace FLaSH.Instagram
{
    class Insta
    {
        private string g_username;
        private string g_password;
        private bool g_isLoggedIn;
        private Dictionary<string, string> g_apiInformation;
        private RestClient g_session;
        private dynamic userObject;

        public Insta(string username, string password)
        {
            this.g_username = username;
            this.g_password = password;
            this.g_isLoggedIn = false;
            g_apiInformation = new Dictionary<string, string>();
            g_apiInformation.Add(
                "user_agent",
                "Instagram 6.21.2 Android (19/4.4.2; 480dpi; 1152x1920; Meizu; MX4; mx4; mt6595; en_US)"
                );

            g_apiInformation.Add(
                "sig_key",
                "25eace5393646842f0d0c3fb2ac7d3cfa15c052436ee86b5406a8433f54d24a5"
                );

            generateIds();

            if (g_session == null)
            {
                g_session = new RestClient("https://instagram.com/api/v1/");
            }
        }

        public Insta(string username, string password, RestClient session) : this(username, password)
        {
            this.g_session = session;
        }

        private void generateIds()
        {
            g_apiInformation.Add("guid", Guid.NewGuid().ToString());
            g_apiInformation.Add("device_id",
                String.Format("android-{0}", g_apiInformation["guid"].Replace("-", "").Substring(0, 16))
            );
        }

        public dynamic Get(string URL)
        {
            if (g_isLoggedIn)
            {
                Console.Out.WriteLine("You must be logged in to access endpoints!");
                return -1;
            }
            else
            {
                var request = new RestRequest(URL, Method.GET);
                return g_session.Execute(request);
            }
        }

        public string Post(string URL, ExpandoObject postData, string contentType = HttpContentTypes.ApplicationJson)
        {
            var request = new RestRequest(URL, Method.POST);

            request.AddHeader("Accept", "*/*");

            g_session.UserAgent = g_apiInformation["user_agent"];

            foreach (var x in postData)
            {
                request.AddParameter(x.Key, x.Value);
            }

            var response = g_session.Execute(request);

            return response.Content;
        }

        public bool Login()
        {

            var dataJson = JsonConvert.SerializeObject(new Dictionary<string, string>()
            {
                 {"username", this.g_username},
                 {"password", this.g_password},
                 {"device_id", g_apiInformation["device_id"]},
                 {"guid", g_apiInformation["guid"] },
                 {"Content-Type", "application/x-www-form-urlencoded;charset=UTF-8" }
            }, Formatting.None);

            dynamic postData = new ExpandoObject();
            postData.ig_sig_key_version = 6;
            postData.signed_body = signMessage(dataJson).ToLower() + "." + dataJson;

            var response = Post("accounts/login/", postData, "application/x-www-form-urlencoded;charset=UTF-8");

            var loginObject = JsonConvert.DeserializeObject(response);

            if( loginObject.status == "ok")
            {
                this.g_isLoggedIn = true;
                this.userObject = loginObject.logged_in_user;
                return true;
            }

            Console.Write(loginObject.status);
            return false;
        }

        private string signMessage(string message)
        {
            var hmac = new System.Security.Cryptography.HMACSHA256(System.Text.ASCIIEncoding.ASCII.GetBytes(g_apiInformation["sig_key"]));
            return BitConverter.ToString(
                    hmac.ComputeHash(System.Text.ASCIIEncoding.ASCII.GetBytes(message)
                )
            ).Replace("-", string.Empty);
        }

        public void SetProxy(System.Net.WebProxy proxy)
        {
            this.g_session.Proxy = proxy;
        }
        
        public void SetPassword(string password)
        {
            this.g_password = password;
        }

        public void SetUsername(string username)
        {
            this.g_username = username;
        }
    }
}
