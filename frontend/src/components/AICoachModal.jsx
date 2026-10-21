import React, { useState, useEffect, useRef } from 'react';
import { X, Mic, MicOff, Send, Sparkles, Volume2, VolumeX, Bot, User } from 'lucide-react';
import axios from 'axios';

export function AICoachModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content:
        "Hey Alex! I'm your AI Growth Coach. I've been watching your channel metrics, retention drop-offs, and comment threads. You haven't posted in 6 days—ask me what to post this week or why your last video underperformed!",
    },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const [voiceEnabled, setVoiceEnabled] = useState(true);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Text to Speech
  const speak = (text) => {
    if (!voiceEnabled || !window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const cleanText = text.replace(/[*#_`]/g, '');
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.rate = 1.05;
    window.speechSynthesis.speak(utterance);
  };

  // Speech to Text (Web Speech API)
  const toggleListening = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert("Speech recognition isn't supported in this browser. Please use Google Chrome or Edge.");
      return;
    }

    if (isListening) {
      setIsListening(false);
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;

    recognition.onstart = () => setIsListening(true);
    recognition.onend = () => setIsListening(false);
    recognition.onerror = () => setIsListening(false);
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript);
      handleSend(transcript);
    };

    recognition.start();
  };

  const handleSend = async (messageText = null) => {
    const textToSend = messageText || input;
    if (!textToSend.trim() || loading) return;

    const userMsg = { role: 'user', content: textToSend };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await axios.post('/api/coach/chat', {
        message: textToSend,
        history: messages.map((m) => ({ role: m.role, content: m.content })),
      });

      const replyMsg = { role: 'assistant', content: res.data.reply };
      setMessages((prev) => [...prev, replyMsg]);

      // Speak response
      if (res.data.audio_text) {
        speak(res.data.audio_text);
      } else {
        speak(res.data.reply);
      }
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content:
            "I couldn't reach the coaching engine right now. Make sure the FastAPI backend is running on port 8000!",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const quickQuestions = [
    'Why did my last video flop?',
    'What should I post this week?',
    'How close am I to monetization?',
  ];

  return (
    <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-[#0f172a] border border-slate-800 rounded-3xl w-full max-w-2xl h-[620px] flex flex-col shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-900/60">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-emerald-400 flex items-center justify-center shadow-md">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <h3 className="font-bold text-white text-base flex items-center gap-2">
                CreatorPilot AI Coach
                <span className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400">
                  Voice Enabled
                </span>
              </h3>
              <p className="text-xs text-slate-400">Siri-like Strategic Manager for Content Creators</p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => {
                setVoiceEnabled(!voiceEnabled);
                if (voiceEnabled) window.speechSynthesis?.cancel();
              }}
              className="p-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition"
              title={voiceEnabled ? 'Mute AI Voice' : 'Enable AI Voice'}
            >
              {voiceEnabled ? <Volume2 className="w-4 h-4 text-emerald-400" /> : <VolumeX className="w-4 h-4 text-slate-500" />}
            </button>
            <button
              onClick={() => {
                window.speechSynthesis?.cancel();
                onClose();
              }}
              className="p-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Chat message history */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          {messages.map((m, idx) => (
            <div
              key={idx}
              className={`flex items-start gap-3 ${m.role === 'user' ? 'flex-row-reverse' : ''}`}
            >
              <div
                className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 ${
                  m.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-indigo-400 border border-slate-700'
                }`}
              >
                {m.role === 'user' ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
              </div>
              <div
                className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
                  m.role === 'user'
                    ? 'bg-indigo-600 text-white rounded-tr-none'
                    : 'bg-slate-800/80 text-slate-200 border border-slate-700/60 rounded-tl-none whitespace-pre-wrap'
                }`}
              >
                {m.content}
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex items-center gap-2 text-xs text-slate-400 italic">
              <Bot className="w-4 h-4 text-indigo-400 animate-spin" />
              CreatorPilot is analyzing your channel stats...
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        {/* Quick prompt chips */}
        <div className="px-6 py-2 flex items-center gap-2 overflow-x-auto border-t border-slate-800/50 bg-slate-900/30">
          <span className="text-[10px] text-slate-500 font-semibold uppercase tracking-wider shrink-0">Ask:</span>
          {quickQuestions.map((q, idx) => (
            <button
              key={idx}
              onClick={() => handleSend(q)}
              className="text-xs px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 border border-slate-700/60 text-slate-300 whitespace-nowrap transition"
            >
              {q}
            </button>
          ))}
        </div>

        {/* Input box */}
        <div className="p-4 bg-slate-900/80 border-t border-slate-800 flex items-center gap-2">
          <button
            onClick={toggleListening}
            className={`p-2.5 rounded-xl transition ${
              isListening
                ? 'bg-rose-600 text-white animate-pulse'
                : 'bg-slate-800 text-slate-300 hover:text-white'
            }`}
            title="Speak into microphone"
          >
            {isListening ? <Mic className="w-5 h-5 text-white" /> : <MicOff className="w-5 h-5" />}
          </button>

          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            placeholder="Ask your coach anything (or tap mic to talk)..."
            className="flex-1 bg-slate-800/80 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition"
          />

          <button
            onClick={() => handleSend()}
            disabled={!input.trim() || loading}
            className="p-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-40 text-white transition"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
