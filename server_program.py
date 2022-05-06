{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "script.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNLI7qcW72em6MqTJ7KOwo6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/johnmunene/Cristians-Algorithm/blob/main/server_program.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6fZHdsF2yAsq",
        "outputId": "30744739-9083-4ab9-d06c-95dae57cd626"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Socket successfully created\n",
            "Socket is listening...\n"
          ]
        }
      ],
      "source": [
        "import socket\n",
        "import datetime\n",
        "\n",
        "# function used to initate clock server\n",
        "def initiateClockServer():\n",
        "\n",
        "  s=socket.socket()\n",
        "  print(\"Socket successfully created\")\n",
        "\n",
        "  # Server port\n",
        "  port=8000\n",
        "\n",
        "  s.bind(('', port))\n",
        "\n",
        "  # Start listening to requests\n",
        "  s.listen(5)\n",
        "  print(\"Socket is listening...\")\n",
        "\n",
        "  # Clock Server running forever\n",
        "  while True:\n",
        "\n",
        "  #Establish a connection with client\n",
        "   connection, address=s.accept()\n",
        "   print('Server connected to', address)\n",
        "\n",
        "   # Respond the client with Server clock time\n",
        "   connection.send(str(\n",
        "       datetime.datetime.now().encode())\n",
        "   )\n",
        "   # Close connection with client process\n",
        "   connection.close()\n",
        "\n",
        "#Driver function\n",
        "if __name__ == '__main__':\n",
        " \n",
        "    # Trigger the Clock Server   \n",
        "    initiateClockServer()\n",
        "\n",
        "\n"
      ]
    }
  ]
}